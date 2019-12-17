from collections import Counter
from pymongo import MongoClient

def get_mongo_db():
    client = MongoClient(f'mongodb+srv://golubeva:golubeva@cluster0-vucbs.azure.mongodb.net/word_count_db', 27017)
    return client.word_count_db.word_count

def word_count():
    text = list(get_mongo_db().find({}))[-1]
    text = text.get('text')
    text = str(text)

    # Cleaning text and lower casing all words
    for char in '-.,\n':
        text=text.replace(char,' ')
    text = text.lower()
    # split returns a list of words delimited by sequences of whitespace (including tabs, newlines, etc, like re's \s) 
    word_list = text.split()
    word_count = Counter(word_list).most_common()
    c = sum(map(lambda x: x[1], word_count))

    collection = get_mongo_db()
    collection.insert_one({'text': (c)})

if __name__ == '__main__':
    word_count()
