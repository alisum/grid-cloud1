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
#    text = list(get_mongo_db().find({}))[-1]
#    text = text.get('text')
    return render_template("answer.html", answer="2")

def get_result():
    subprocess.run(["az", "vm", "start", "--name", "grid-cloud", "--resource-group", "grid-cloud"])
    subprocess.run(["ssh", "-i" "name" "mgolubeva@40.127.108.18" "python3" "app.py"])

if __name__ == '__main__':
    app.run()
