from flask import Flask
from flask import request
from flask import render_template
from flask import redirect
from flask import url_for
import os

import pymongo
from pymongo import MongoClient
import pprint

app = Flask(__name__)

data = {
        'question' : 'Which web framework do you use?',
        'fields'   : ['Flask', 'Django', 'web2py'],
        'votes'   : {'Flask':0, 'Django':0, 'web2py':0}
        }

# Set up the database
client = MongoClient('mongodb://localhost:27017')
dbnames = client.database_names()
db = client.poll # get the database
poll_data = db.poll_data # get the collection

if poll_data.count() == 0:
    poll_data.insert_one(data)
    print('created db')
else:
    print('db already exists')

@app.route('/')
def root():
    p_data = poll_data.find_one()
    return render_template('poll.html', data=p_data)

@app.route('/poll', methods=['POST'])
def poll():
    p_data = poll_data.find_one() # get the document
    vote = request.form['field']
    vote_count = p_data['votes'][vote]
    vote_count += 1
    poll_data.update_one(
            {'question' : 'Which web framework do you use?'},
            {'$set': {'votes.' + vote : vote_count }}
        )
    return render_template('thankyou.html', data=p_data)

@app.route('/result')
def result():
    p_data = poll_data.find_one()
    vote = p_data['votes']
    return render_template('result.html', data=p_data, votes=vote)

@app.route('/test')
def test():
    return redirect(url_for('result'))

if __name__ == "__main__":
    app.run(debug=True)
