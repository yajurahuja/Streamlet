class vote:
    def __init__(self, signature, block, id_):
        self.signature = signature
        self.block = block
        self.id = id_

    def isequal(self, vote):
        return self.signature == vote.signature and self.block.isequal(vote.block) and self.id == vote.id

        
    
    