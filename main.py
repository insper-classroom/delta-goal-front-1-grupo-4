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
    return render_template('login.html')

@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    error_message = ""
    return render_template('cadastro.html', error_message=error_message)

@app.route("/esqueci_senha", methods=["GET", "POST"])
def esqueci_senha():
    error_message = None
    return render_template('redsenha.html', error_message=error_message)

@app.route("/sucesso_redefinicao")
def sucesso_redefinicao():
    return render_template('sucesso.html')

@app.route("/home")
@login_required
def home():
    return render_template('inicial.html')

def get_user_data(username):
    user_data = session['username']

    return user_data

@app.route("/perfil")
def perfil():
    if 'username' in session:
        username = session['username']
        user_data = get_user_data(username)
        if user_data:
            return render_template('perfil.html', user_data=user_data)
    
    flash("Você precisa estar logado para acessar esta página.")
    return redirect(url_for('login'))


@app.route('/ver_dados')
def ver_dados():
    return 'Dados'
    
if __name__ == '__main__':
    app.run(debug=True, port=8080)
