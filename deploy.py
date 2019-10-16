from flask import Flask, render_template
from wordapi import generateGame

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/getWordGame')
def wordGame():
    return generateGame(4, 6)
