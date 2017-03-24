from flask import Flask
from flask import request
from flask import render_template
import os
app = Flask(__name__)

filename = 'data.txt'

poll_data = {
        'question' : 'Which web framework do you use?',
        'fields'   : ['Flask', 'Django', 'web2py']
        }

@app.route('/')
def root():
    return render_template('poll.html', data=poll_data)

@app.route('/poll', methods=['POST'])
def poll():
    vote = request.form['field']

    out = open(filename, 'a')
    out.write(vote + '\n')
    out.close()

    return render_template('thankyou.html', data=poll_data)

if __name__ == "__main__":
    app.run()
