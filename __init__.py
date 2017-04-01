import os
from flask import Flask

import pymongo
from pymongo import MongoClient
import pprint

app = Flask(__name__)
app.config['DEBUG'] = True
app.config.from_object('config')

# Set up the database
client = MongoClient('mongodb://localhost:27017')
db = client.poll

data = {
        'question' : 'Which web framework do you use?',
        'fields'   : ['Flask', 'Django', 'web2py'],
        'votes'   : {'Flask':0, 'Django':0, 'web2py':0}
        }
