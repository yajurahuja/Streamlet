from meta_data import meta_data

class block:
    def __init__(self, parent, epoch, txs):
        self.parent = parent #stores the parent hash
        self.epuch = epoch #current epoch number
        self.txs = txs #list of transactions
        self.meta_data = meta_data() #any meta data to store 

    def signature_encode(self):
        #TODO
        return False

    def compare_txs(self, other_txs):
        return self.txs == other_txs

    def isequal(self, other):
        return self.parent == other.parent and self.epoch = other.epoch and self.compare_txs(other.txs)

    def hash(self, hasher):
        #TODO: figure out hashing






    