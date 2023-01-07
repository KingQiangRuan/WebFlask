#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
@File: main.py
@Date: 2023/01/07 14:32:10
@Author: qiang
@Version: 1.0:
@License: Copyright (c) 2022-2023, All rights reserved.
@Decription: xxxxxx
'''

from flask import Flask,render_template,request,redirect
from flask import session

app = Flask(__name__)
app.secret_key = 'fhdsruanqiang233hfdsfbj'
app.debug=True

 
@app.route('/', methods=['GET', 'POST'])
@app.route('/index.html', methods=['GET', 'POST'])
def homepage():
    # 指定文件路径
    page = render_template('index.html', templat_folder='templates', static_folder='static')
    return page

@app.route('/cards.html', methods=['GET', 'POST'])
def CardsPage():
    # 指定文件路径
    page = render_template('cards.html', templat_folder='templates', static_folder='static')
    return page

@app.route('/charts.html', methods=['GET', 'POST'])
def ChartsPage():
    # 指定文件路径
    page = render_template('charts.html', templat_folder='templates', static_folder='static')
    return page


def get_data_from_web():
    pass



if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5600, debug=True)