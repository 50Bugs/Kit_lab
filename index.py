import os
#import url
import requests
from lxml import html
from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from flask import request
from flask import Flask
from flask import Response
import flask

app = Flask(__name__, template_folder='template')
app.config["IMAGE_UPLOADS"] = './static'

@app.route("/market", methods=['GET', 'POST'])
def f1():
    if request.method == 'POST':
        return request.form['name']+" "+request.form['surname']+" "+request.form['adress']+" "+request.form['count']
    return render_template('index.html')

@app.route("/post", methods=['GET', 'POST'])
def f2():
    if request.method == 'POST':
        return request.form['adress']+" "+request.form['name']+" "+request.form['surname']+" "+request.form['count']

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5002))
    app.run(host='0.0.0.0', port=port)
