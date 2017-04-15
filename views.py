from flask import request
from flask import render_template
from flask import redirect
from flask import url_for
from __init__ import app
from __init__ import poll_data
from models import Question
import pprint


# Get the first question always
ques = Question()
ques.get_first()

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500

@app.route('/')
@app.route('/home')
def home():
    ques.get_first()
    return render_template('poll.html', data=ques.question)

@app.route('/poll', methods=['POST'])
def poll():
    vote = request.form['field']
    ques.update_poll(ques.question, vote)
    return render_template('thankyou.html', data=ques.question)

@app.route('/result')
def result():
    vote = ques.get_result(ques.question)
    return render_template('result.html', data=ques.question, votes=vote)

@app.route('/test')
def test():
    return redirect(url_for('home'))
