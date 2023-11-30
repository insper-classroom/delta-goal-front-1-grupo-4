from functools import wraps
from flask import Flask, request, redirect, url_for, render_template, flash, session
from flask_pymongo import PyMongo
from flask_mail import Mail, Message
import os
import re
from bson import json_util

app = Flask('Delta_Goal_Front')

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
    # if request.method == "POST":
    #     email = request.form.get("email")
    #     senha = request.form.get("password")

    #     user = mongo.db.users.find_one({"email": email, "senha": senha})

    #     if user:
    #         session['username'] = user['nome']
    #         return redirect(url_for('home'))
    #     else:
    #         flash('E-mail ou senha incorretos. Tente novamente!')
    #         return redirect(url_for('login'))
    # else:
    return render_template('login.html')

@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    error_message = ""
    # if request.method == "POST":
    #     nome = request.form.get("nome")
    #     email = request.form.get("email")
    #     senha = request.form.get("senha")
    #     confirma_senha = request.form.get("confirma_senha")

    #     if len(senha) < 8 or not re.search(r'\d', senha):
    #         error_message = "A senha deve ter pelo menos 8 caracteres e incluir pelo menos um número."
    #     elif senha != confirma_senha:
    #         error_message = "As senhas não coincidem"
    #     elif mongo.db.users.find_one({"email": email}):
    #         error_message = "E-mail já cadastrado"
    #     else:
    #         # Armazenando a senha em texto puro (não recomendado para produção)
    #         mongo.db.users.insert_one({"nome": nome, "email": email, "senha": senha})
    #         flash("Cadastro realizado com sucesso!")
    #         return redirect(url_for('login'))

    return render_template('cadastro.html', error_message=error_message)

@app.route("/esqueci_senha", methods=["GET", "POST"])
def esqueci_senha():
    error_message = None

    # if request.method == "POST":
    #     email = request.form.get("email")
        
    #     user = mongo.db.users.find_one({"email": email})
    #     if user:
    #         msg = Message("Redefinição de Senha", sender="xxxx@gmail.com", recipients=[email])
    #         msg.body = "Link para redefinir a senha"
    #         mail.send(msg)
    #         flash("Instruções para redefinir a senha foram enviadas para o seu e-mail.")
    #     else:
    #         error_message = "E-mail não encontrado."

    #     return redirect(url_for('esqueci_senha'))

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
    # pegando nome do user pela session
    user_data = session['username']

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


# @app.route('/ver_dados')
# def ver_dados():
#     try:
#         dados = mongo.db.users.find()  
#         dados_serializaveis = json_util.dumps(dados)
#         return dados_serializaveis
#     except Exception as e:
#         return str(e)
    
if __name__ == '__main__':
    app.run(port=8080)