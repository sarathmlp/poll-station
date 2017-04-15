from __init__ import poll_data
from bson import ObjectId
from config import QUES_PER_PAGE
import pprint

class Question:
    def __init__(self):
        self.question = {}
        self.last_id = 0

    def get_first(self):
        cursor = poll_data.find().limit(QUES_PER_PAGE)
        for data in cursor:
            self.question = data
            self.last_id = data['_id']

    def get_next(self):
        cursor = poll_data.find({'_id': {'$gt': ObjectId(self.last_id)}}).limit(QUES_PER_PAGE)
        for data in cursor:
            self.question = data
            self.last_id = data['_id']

    def update_poll(self, question, vote):
        self.question['votes'][vote] += 1
        result = poll_data.update_one(
                    {'question' : question['question']},
                    {'$set':
                        {'votes.' + vote : self.question['votes'][vote]}
                        }
                    )
        if result.modified_count != 1:
            raise ValueError('failed to update db')

    def get_result(self, question):
        p_data = poll_data.find_one({'question' : question['question']})
        return p_data['votes']
