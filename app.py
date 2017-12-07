from flask import Flask, render_template
import requests

from flask import flash, redirect, request, session, abort
import os

#Application initialization
app = Flask(__name__)

#URL to function mappings
@app.route('/')
def index():
    return render_template('index1.html')

@app.route('/login/', methods = ['POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            #return redirect(url_for('home'))
            error = "ok"
    return render_template('login.html', error=error)

if __name__ == '__main__':
    app.run(host='0.0.0.0')