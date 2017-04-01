from flask import request
from flask import render_template
from flask import redirect
from flask import url_for
from __init__ import app
from __init__ import poll_data
from __init__ import ques
import pprint


# ---------- Begin the App ----------------- #
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500


@app.route('/')
@app.route('/root')
def root():
    p_data = ques.qlist[0]
    return render_template('poll.html', data=p_data)

@app.route('/poll', methods=['POST'])
def poll():
    vote = request.form['field']
    question = ques.get_question(vote)
    if question is not None:
        question['votes'][vote] += 1

    poll_data.update_one(
            {'index' : question['index']},
            {'$set': {'votes.' + vote : question['votes'][vote]}}
        )
    return render_template('thankyou.html', data=question)

@app.route('/result')
def result():
    p_data = poll_data.find_one({'index': 1})
    vote = p_data['votes']
    return render_template('result.html', data=p_data, votes=vote)

@app.route('/test')
def test():
    return redirect(url_for('root'))
