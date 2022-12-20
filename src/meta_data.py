import time
class meta_data:
    def __init__(self):
        self.votes = []
        self.notarized = False
        self.finalized = False
        self.time_stamp = time.time() #TODO: fix the time

    def is_notarized(self):
        return self.notarized

    def is_finalized(self):
        return self.finalized

    def check_vote(self, vote):
        for v in self.votes:
            if v.isequal(vote):
                return True
        return False
