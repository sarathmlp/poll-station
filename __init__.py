import os
import ast
from flask import Flask

import pymongo
from pymongo import MongoClient
import pprint
from models import Question

app = Flask(__name__)
app.config.from_object('config')

# Initialize logging
if not app.debug:
    import logging
    from logging.handlers import RotatingFileHandler
    file_handler = RotatingFileHandler('/tmp/poll_station.log', 'a', 1 * 1024 * 1024, 10)
    file_handler.setFormatter(
     logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('hurray')

# Initialize the database
client = MongoClient('mongodb://localhost:27017')
db = client.poll
poll_data = db.poll_data

if poll_data.count() == 0:
    f = open('input.json', 'r')
    data = f.read()
    qlist = ast.literal_eval(data)
    result = poll_data.insert_many(qlist)
    app.logger.debug(result.inserted_ids)

ques = Question()
for q in poll_data.find():
    ques.qlist.append(q)
