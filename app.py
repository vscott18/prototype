from flask import Flask, render_template
import requests

#Application initialization
app = Flask(__name__)

#URL to function mappings
@app.route('/')
def index():
    return render_template('index1.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0')