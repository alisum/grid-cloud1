import re
import subprocess
import time
from concurrent.futures import ThreadPoolExecutor

from flask import Flask, render_template, request, redirect
from pymongo import MongoClient

def get_mongo_db():
    client = MongoClient(f'mongodb+srv://golubeva:golubeva@cluster0-vucbs.azure.mongodb.net/word_count_db', 27017)
    return client.word_count_db

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route('/')
def hello():
    user = { 'nickname': 'Nickname' } # выдуманный пользователь
    return render_template("index.html",
        title = 'Home',
        user = user)

@app.route('/count', methods=['POST'])
def word_count():
    rq_result = get_mongo_db().word_count.insert_one({'text': (request.form['text'])})
    get_result()
    return redirect('/answer')
    
@app.route('/answer')
def result():
    text = list(get_mongo_db().word_count.find().sort([('$natural', -1)]).limit(1))
    return render_template("answer.html", answer=text[0]['result'])

def get_result():
    print('startng vm')
    subprocess.run(["az", "vm", "start", "--name", "grid-cloud2", "--resource-group", "grid-cloud"])
    print('running app')
    subprocess.run(["ssh", "-o", "StrictHostKeyChecking=no", "-i", "name", "mgolubeva@52.169.147.155", "python3", "app.py"])

if __name__ == '__main__':
    app.run()
