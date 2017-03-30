from __future__ import print_function
import os
import unittest
import poll

class PollTestCase(unittest.TestCase):
    def setUp(self):
        if os.path.exists(poll.filename):
            os.remove(poll.filename)
        self.app = poll.app.test_client()

    def tearDown(self):
        if os.path.exists(poll.filename):
            os.remove(poll.filename)

    def test_main_page(self):
        rv = self.app.get('/')
        self.assertRegex(rv.data.decode('utf-8'), '<title>Which web framework do you use\?</title>')
        self.assertRegex(rv.data.decode('utf-8'), "<input type='radio' name='field' value=Flask> Flask<br>") 

    @unittest.expectedFailure
    def test_empty_result(self):
        rv = self.app.get('/result')
        self.assertEqual(rv.status_code, 200)
        self.assertRegex(rv.data.decode('utf-8'), 'No results yet')

if __name__ == '__main__':
    unittest.main()
