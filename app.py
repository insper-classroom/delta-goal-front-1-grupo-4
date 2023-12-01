from functools import wraps
from flask import Flask, request, redirect, url_for, render_template, flash, session
from flask_pymongo import PyMongo
from flask_mail import Mail, Message
import os
import re
from bson import json_util
from zonas import calculate_zone_percentages, data
from cruzamento import extrair_informacoes_palmeiras

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb+srv://admin:admin@sprint-20232-grupo4.gcd9bsz.mongodb.net/delta_goal"
mongo = PyMongo(app)
app.secret_key = '123'

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'xxxx@gmail.com.br'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)

email_password = os.environ.get('EMAIL_PASSWORD')

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            flash('Você precisa estar logado para acessar esta página.', 'warning')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email")
        senha = request.form.get("password")

        user = mongo.db.users.find_one({"email": email, "senha": senha})

        if user:
            session['username'] = user['nome']
            return redirect(url_for('home'))
        else:
            flash('E-mail ou senha incorretos. Tente novamente!')
            return redirect(url_for('login'))
    else:
        return render_template('login.html')

@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    error_message = ""
    if request.method == "POST":
        nome = request.form.get("nome")
        email = request.form.get("email")
        senha = request.form.get("senha")
        confirma_senha = request.form.get("confirma_senha")

        if len(senha) < 8 or not re.search(r'\d', senha):
            error_message = "A senha deve ter pelo menos 8 caracteres e incluir pelo menos um número."
        elif senha != confirma_senha:
            error_message = "As senhas não coincidem"
        elif mongo.db.users.find_one({"email": email}):
            error_message = "E-mail já cadastrado"
        else:
            # Armazenando a senha em texto puro (não recomendado para produção)
            mongo.db.users.insert_one({"nome": nome, "email": email, "senha": senha})
            flash("Cadastro realizado com sucesso!")
            return redirect(url_for('login'))

    return render_template('cadastro.html', error_message=error_message)

@app.route("/esqueci_senha", methods=["GET", "POST"])
def esqueci_senha():
    error_message = None

    if request.method == "POST":
        email = request.form.get("email")
        
        user = mongo.db.users.find_one({"email": email})
        if user:
            msg = Message("Redefinição de Senha", sender="xxxx@gmail.com", recipients=[email])
            msg.body = "Link para redefinir a senha"
            mail.send(msg)
            flash("Instruções para redefinir a senha foram enviadas para o seu e-mail.")
        else:
            error_message = "E-mail não encontrado."

        return redirect(url_for('esqueci_senha'))

    return render_template('redsenha.html', error_message=error_message)

@app.route("/sucesso_redefinicao")
def sucesso_redefinicao():
    return render_template('sucesso.html')

@app.route("/home")
@login_required
def home():
    return render_template('inicial.html')

def get_user_data(username):
    # Recupere os dados do usuário do banco de dados com base no nome de usuário
    user_data = mongo.db.users.find_one({"nome": username})
    return user_data

@app.route("/perfil")
def perfil():
    # Verifique se o usuário está logado
    if 'username' in session:
        username = session['username']
        user_data = get_user_data(username)
        if user_data:
            return render_template('perfil.html', user_data=user_data)
    
    # Se o usuário não estiver logado ou os dados do usuário não forem encontrados, redirecione para a página de login
    flash("Você precisa estar logado para acessar esta página.")
    return redirect(url_for('login'))

@app.template_filter('convert_to_seconds')
def convert_to_seconds(time_str):
    hours, minutes, seconds = map(int, time_str.split(':'))
    return hours * 3600 + minutes * 60 + seconds

app.jinja_env.filters['convert_to_seconds'] = convert_to_seconds

@app.template_filter('minus_five_seconds')
def minus_five_seconds(seconds):
    return max(seconds - 5, 0)

@app.route("/partida")
@login_required
def partida():

    zone_percentages = calculate_zone_percentages(data)
    zone_percentages_formatted = {zone: f"{percentage:.1f}%" for zone, percentage in zone_percentages.items()}
    app.jinja_env.filters['convert_to_seconds'] = convert_to_seconds
    app.jinja_env.filters['minus_five_seconds'] = minus_five_seconds
    cruzamentos_palmeiras = extrair_informacoes_palmeiras(data)


    destaques = {
        'sep': [
            {'nome': 'G Gomes', 'numero': 16, 'imagem': 'static/img/campo.png'},
            {'nome': 'Luan', 'numero': 15, 'imagem': 'static/img/veiga.png'},
            {'nome': 'Rony ', 'numero': 13, 'imagem': 'static/img/veiga.png'},
            {'nome': 'Fabinho', 'numero': 12, 'imagem': 'static/img/veiga.png'},
            {'nome': 'Arthur', 'numero': 12, 'imagem': 'static/img/bragantino.png'},
          

            # Adicione mais jogadores conforme necessário
        ],
        'rbb': [
            {'nome': 'Sasha', 'numero': 9, 'imagem': 'static/img/gabriel-menino.jpg'},
            {'nome': 'E. Santos ', 'numero': 7, 'imagem': 'static/img/veiga.png'},
            {'nome': 'B. Goncalves	', 'numero': 6, 'imagem': 'static/img/veiga.png'},
            {'nome': 'Natan', 'numero': 6, 'imagem': 'static/img/veiga.png'},
            {'nome': 'Juninho Capixaba	', 'numero': 5, 'imagem': 'static/img/veiga.png'},

            # Adicione mais jogadores conforme necessário
        ]
    }
    return render_template('partida.html', destaques=destaques, porcentagens=zone_percentages_formatted,cruzamentos=cruzamentos_palmeiras)


@app.route('/ver_dados')
def ver_dados():
    try:
        dados = mongo.db.users.find()  
        dados_serializaveis = json_util.dumps(dados)
        return dados_serializaveis
    except Exception as e:
        return str(e)
    
if __name__ == '__main__':
    app.run(port=8080)

