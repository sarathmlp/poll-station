from flask import Flask
import pymongo
from pymongo import MongoClient
import pprint

app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017')
db = client.test_database
posts = db.posts

for post in posts.find():
    pprint.pprint(post)


if __name__ == '__main__':
    app.run()
