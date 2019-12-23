#-*- coding:utf-8 -*-

from flask import Flask, render_template,request,flash,redirect,session
import importlib,sys
from tool import create_game
import random
importlib.reload(sys)



app = Flask(__name__)
app.secret_key = 'NavigateyourcodewitheaseInselectpublicrepositoriesyoucannowclickonfunctionandmethodcalls'



@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.rotue('/game', methods=['GET', 'POST'])
def get_data():
    data = create_game.inspection()
    return data


if __name__ == '__main__':
    app.run(port=8000)





