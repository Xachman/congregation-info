  
from flask import Flask, render_template, request, abort
import sys
from datetime import datetime
from pathlib import Path
from pprint import pprint
from os import environ
import schedule as sched
import logger

app = Flask(__name__)


@app.route('/')
def main(path=''):
    return render_template('layout.html', content='time')


@app.route('/schedule')
def schedule(path=''):
    data = sched.getToday()
    logger.log(data)
   # return render_template('schedule.html')
    return render_template('layout.html', content='schedule', group=data.get('group', 'none'), type=data.get('type', 'none'))

DEV = False
if environ.get('DEV') == 'true':
    DEV = True
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080, debug=DEV)