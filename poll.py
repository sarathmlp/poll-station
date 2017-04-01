from flask import request
from flask import render_template
from flask import redirect
from flask import url_for
from __init__ import app
from __init__ import db
from __init__ import data

# Get the collection
poll_data = db.poll_data

if poll_data.count() == 0:
    poll_data.insert_one(data)
    print('created db')
else:
    print('db already exists')

@app.route('/')
@app.route('/root')
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
    return redirect(url_for('root'))

if __name__ == "__main__":
    app.run(debug=True)
