from functools import wraps
from flask import Flask, request, redirect, url_for, render_template, flash, session
from flask_pymongo import PyMongo
from flask_mail import Mail, Message
import os
import re
from bson import json_util

app = Flask('Delta_Goal_Front')
app.config['SECRET_KEY'] = 'dg123'

@app.template_filter('convert_to_seconds')
def convert_to_seconds(time_str):
    hours, minutes, seconds = map(int, time_str.split(':'))
    return hours * 3600 + minutes * 60 + seconds

app.jinja_env.filters['convert_to_seconds'] = convert_to_seconds

@app.template_filter('minus_five_seconds')
def minus_five_seconds(seconds):
    return max(seconds - 5, 0)

@app.route("/")
def redirect_to_login():
    return redirect(url_for('login'))

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
def home():
    return render_template('inicial.html')

@app.route('/ver_dados')
def ver_dados():
    return 'Dados'

@app.route("/partida")
def partida():
    return render_template('partida2.html')
    # return render_template('partida2.html', destaques=destaques, porcentagens=zone_percentages,porcentagens_bragan=zone_percentages_bragan,cruzamentos=cruzamentos_palmeiras)
    
if __name__ == '__main__':
    app.run(debug=True, port=8080)
