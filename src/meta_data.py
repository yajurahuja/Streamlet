import time
class meta_data:
    def __init__(self):
        self.votes = [] #votes for the block
        self.notarized = False #flag if the block is notaized
        self.finalized = False #flag if the block is finalized
        self.time_stamp = time.time() #TODO: fix the time

    #returns true if the block has been notarized
    def is_notarized(self):
        return self.notarized

    #returns true if the block has been finalized
    def is_finalized(self):
        return self.finalized

    #checks if a vote already exists in the vote list of the block
    def check_vote(self, vote):
        for v in self.votes:
            if v.isequal(vote):
                return True
        return False
