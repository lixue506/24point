#-*- coding:utf-8 -*-

from flask import Flask, render_template,request
import importlib,sys
from tool import *
import json
importlib.reload(sys)



app = Flask(__name__)
app.secret_key = 'Navigaonfunctionandmethodcalls'



@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/index', methods=['GET', 'POST'])
def back_index():
    return render_template('index.html')

@app.route('/game', methods=['GET', 'POST'])
def tran():
    return render_template('game.html')

@app.route('/game_sub', methods=['GET', 'POST'])
def get_submit():
    cal = request.values['cal']
    r = eval(cal)
    return json.dumps({'result':'success' if r==24 else 'error'})

@app.route('/game_help', methods=['GET', 'POST'])
def get_help():
    class_app = create_game()
    lst = [int(request.values['num'+str(i)]) for i in range(6,10)]
    all_r = class_app.test24(v=lst)
    return json.dumps({'all_result':all_r})

if __name__ == '__main__':
    app.run(port=8000)





