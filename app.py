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
    rq_result = get_mongo_db().tasks.insert_one({'text': (request.form['text'])})
    get_result()
    return redirect(f'/result/{str(rq_result.inserted_id)}')
    result(request.form['text'])
	
def get_result():
    subprocess.Popen("bash server.sh", shell=True)

if __name__ == '__app__':
    app.run()
