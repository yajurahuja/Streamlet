from meta_data import meta_data

class block:
    def __init__(self, parent, epoch, txs):
        self.parent = parent #stores the parent hash
        self.epoch = epoch #current epoch number
        self.txs = txs #list of transactions
        self.meta_data = meta_data() #any meta data to store 

    def signature_encode(self):
        #TODO
        sig_str = "{} {} {}".format(self.parent, self.epoch, self.txs)
        signature = list(bytes(sig_str, 'utf-8'))
        return signature

    def compare_txs(self, other_txs):
        return self.txs == other_txs

    def isequal(self, other):
        return self.parent == other.parent and self.epoch = other.epoch and self.compare_txs(other.txs)

    def hash(self, hasher):
        #TODO: figure out hashing
        block_str = str((self.parent, self.epoch, self.txs))
        hasher.update(block_str)
        return hasher.finalize





    