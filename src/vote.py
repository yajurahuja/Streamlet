from block import block
class vote:
    def __init__(self, signature, block, id_):
        self.signature = signature
        self.block = block
        self.id = id_

    def isequal(self, vote):
        return self.signature == vote.signature and self.block.isequal(vote.block) and self.id == vote.id

    def print_(self):
        print("leader who proposed the block: ", self.id)
        self.block.print_(0)
        #print("Proposal signature: ", self.signature)
        
        
    
    
    