#!/Users/saratv/Sandbox/python/test/venv/bin/python

from flask import Flask
from flask import request
from flask import render_template
import os
app = Flask(__name__)

@app.route('/')
def root():
    return render_template('poll.html')


if __name__ == "__main__":
    app.run()
