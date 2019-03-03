  
from flask import Flask, render_template, request, abort
import sys
from datetime import datetime
from pathlib import Path
from pprint import pprint
from os import environ
app = Flask(__name__)


@app.route('/')
def main(path=''):
    return render_template('time.html')


@app.route('/schedule')
def main(path=''):
    return render_template('time.html')

DEV = False
if environ.get('DEV') == 'true':
    DEV = True
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080, debug=DEV)