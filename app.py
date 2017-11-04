
from flask import Flask, redirect, session
from flask import render_template
from flask import request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import sys

#Application initialization
app = Flask(__name__)

#URL to function mappings
@app.route('/')

if __name__ == '__main__':
    app.run()