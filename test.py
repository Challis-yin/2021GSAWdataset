# -*- coding: utf-8 -*-
from flask import Flask ,jsonify,render_template,url_for,redirect,abort, request

app = Flask('kkk')
@app.route('/', methods=['GET', 'POST'])
def test1():
    return render_template("index.html")

@app.route('/search', methods=['GET', 'POST'])
def test2():
    return render_template("search.html")

@app.route('/summary', methods=['GET', 'POST'])
def test3():
    return render_template("summary.html")
    
@app.route('/details', methods=['GET', 'POST'])
def test4():
    return render_template("details.html")

app.run(host="0.0.0.0")

