import flask_pymongo
from flask import Flask, render_template, request, redirect, url_for, session, flash
import requests

app = Flask('DeltaGoal')


@app.route('/')
def inicial():
    return render_template('inicial.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        print('banana')
        email = request.form.get('email')
        password = request.form.get('password')
        if email and password:
            response = requests.post('http://localhost:5000/login', json={'email': email, 'password': password})
            print(response.status_code)
            if response.status_code == 200:
                print('11111111111111')
                return render_template('inicial.html')
            else:
                flash('Email ou senha inválidos')
                return redirect(url_for('login'))
        else:
            flash('Email ou senha inválidos')
            return redirect(url_for('login'))
    elif request.method == 'GET':
        return render_template('login.html')



if __name__ == '__main__':
    app.run(debug=True, port=5001)