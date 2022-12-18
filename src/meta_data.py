import time
class meta_data:
    def __init__(self):
        self.vote = []
        self.notarized = False
        self.finalized = False
        self.time_stamp = time.time() #TODO: fix the time

    def is_notarized(self):
        return self.notarized

    def is_finalized(self):
        return self.finalized
