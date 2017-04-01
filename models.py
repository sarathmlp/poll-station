class Question:
    def __init__(self):
        self.qlist = []

    def get_question(self, vote):
        for q in self.qlist:
            if vote in q['votes']:
                return q
            else:
                return None

