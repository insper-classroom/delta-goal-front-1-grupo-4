from functools import wraps
from flask import Flask, request, redirect, url_for, render_template, flash, session
from flask_pymongo import PyMongo
from flask_mail import Mail, Message
import os
import re
import requests
from bson import json_util
from zonas import calculate_line_break_percentages_v4,data, zones_of_interest_v4,aaaa

app = Flask("Delta_Goal_Front")
app.config["SECRET_KEY"] = "dg123"


@app.template_filter("convert_to_seconds")
def convert_to_seconds(time_str):
    hours, minutes, seconds = map(int, time_str.split(":"))
    return hours * 3600 + minutes * 60 + seconds


app.jinja_env.filters["convert_to_seconds"] = convert_to_seconds


@app.template_filter("minus_five_seconds")
def minus_five_seconds(seconds):
    return max(seconds - 5, 0)


@app.route("/")
def redirect_to_login():
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")


@app.route("/cadastro", methods=["GET", "POST"])
def cadastro():
    error_message = ""
    return render_template("cadastro.html", error_message=error_message)


@app.route("/esqueci_senha", methods=["GET", "POST"])
def esqueci_senha():
    error_message = None
    return render_template("redsenha.html", error_message=error_message)


@app.route("/sucesso_redefinicao")
def sucesso_redefinicao():
    return render_template("sucesso.html")


@app.route("/home")
def home():
    return render_template("inicial.html")


@app.route("/ver_dados")
def ver_dados():
    return "Dados"


@app.route("/cruzamentos")
def cruzamentos():
    destaques = requests.get("http://localhost:5000/cruzamentos/destaques")
    destaques = destaques.json()["destaques"]
    porcentagens = requests.get("http://localhost:5000/cruzamentos/zonas")
    porcentagens = porcentagens.json()
    zone_percentages = porcentagens["zonas"]["pal"]
    zone_percentages_bragan = porcentagens["zonas"]["red"]
    desfechos = requests.get("http://localhost:5000/cruzamentos/desfechos")
    desfechos = desfechos.json()
    desfechos = desfechos["desfechos"]
    cruzamentos = requests.get("http://localhost:5000/cruzamentos")
    cruzamentos_palmeiras = cruzamentos.json()["cruzamentos"]["pal"]
    cruzamentos_bragantino = cruzamentos.json()['cruzamentos']['red']
    return render_template(
        "cruzamentos.html",
        desfechos=desfechos,
        destaques=destaques,
        porcentagens=zone_percentages,
        porcentagens_bragan=zone_percentages_bragan,
        cruzamentos=cruzamentos_palmeiras, cruzamentos1=cruzamentos_bragantino,
    )

@app.route("/quebras")
def quebras():
    destaques = requests.get("http://localhost:5000/quebra_linha/destaques")
    destaques = destaques.json()["destaques"]
    # quebras = requests.get("http://localhost:5000/quebra_linha")
    # quebras_palmeiras = quebras.json()["quebras_linha"]["pal"]
    quebra_palmeiras= data['time']['1']['rupturas']
    quebra_bragantino= data['time']['5']['rupturas']
    desfechos=aaaa(data)
    porcentagem_quebra= calculate_line_break_percentages_v4(data, zones_of_interest_v4)
    return render_template("quebras_de_linha.html",destaques=destaques, porcentagem_quebra= porcentagem_quebra, quebras=quebra_palmeiras, quebras1=quebra_bragantino, desfechos=desfechos)

@app.route("/partidas")
def partidas():
    return render_template("partidas.html")

if __name__ == "__main__":
    app.run(debug=True, port=8080)
