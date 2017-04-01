from flask import Flask
import pymongo
from pymongo import MongoClient
import pprint
import ast
from models import Question

client = MongoClient('mongodb://localhost:27017')

db = client.poll
poll_data = db.poll_data

if poll_data.count() == 0:
    print ('Creating db')
    f = open('input.json', 'r')
    data = f.read()
    q_list = ast.literal_eval(data)
    result = poll_data.insert_many(q_list)
    print (result.inserted_ids)

ques = Question()
for q in poll_data.find():
    ques.q_list.append(q)

for q in ques.q_list:
    pprint.pprint(q)
