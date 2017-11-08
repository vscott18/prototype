
from flask import Flask, redirect, session
from flask import render_template
from flask import request
from flask_sqlalchemy import SQLAlchemy
from database_functions import *
from database_test import DatabaseTest
from flask_migrate import Migrate
from subprocess import call
import sys

#Application initialization
app = Flask(__name__)

#URL to function mappings
@app.route('/', methods=['GET', 'POST'])
def home_page():
    return render_template('index1.html')

@app.route('/processquery', methods = ['POST'])
def processquery():
    db = Database()
    db.close()
if __name__ == '__main__':
    app.run()