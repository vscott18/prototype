from flask import Flask, redirect, session
from flask import render_template
# from flask import request
# from flask_sqlalchemy import SQLAlchemy
# # from database_functions import *
# from flask_migrate import Migrate
# from subprocess import call
# import sys

# #Application initialization
# app = Flask(__name__)

# #URL to function mappings
# @app.route('/')
# def home_page():
#     return render_template('index1.html')

# # @app.route('/processquery', methods = ['POST'])
# # def processquery():
# #     db = Database()
# #     db.close()

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', debug = True)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index1.html')

if __name__ == '__main__':
    app.run(debug=True)