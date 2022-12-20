from meta_data import meta_data

class block:
    def __init__(self, parent, epoch, txs):
        self.parent = parent #stores the parent hash
        self.epoch = epoch #current epoch number
        self.txs = txs #list of transactions
        self.meta_data = meta_data() #any meta data to store 

    def __bytes__(self):
        sig_str = "{} {} {}".format(self.parent, self.epoch, self.txs)
        return bytes(sig_str, 'utf-8')

    def signature_encode(self):
        #TODO
        sig_str = "{} {} {}".format(self.parent, self.epoch, self.txs)
        print(sig_str)
        signature = bytes(sig_str, 'utf-8')
        print(signature)
        return signature

    def compare_txs(self, other_txs):
        return self.txs == other_txs

    def isequal(self, other):
        return self.parent == other.parent and self.epoch == other.epoch and self.compare_txs(other.txs)

    def get_hash(self, common_hash):
        h = common_hash.get_hasher()
        h.update(bytes(self))
        return h.finalize

    def check_vote(self, vote):
        self.meta_data.check_vote()

    def add_vote(self, vote):
        self.meta_data.votes.append(votes)

    def get_vote_count(self):
        return len(self.meta_data.votes)

    def notarize(self):
        self.meta_data.notarized = True
        
    def is_notarized(self):
        return self.meta_data.is_notarized()

if __name__ == "__main__":
    b1 = block("123", 1, ["hey", "hello", "how are you"])
    b2 = block("123", 1, ["hey", "hello", "how are you"])
    print(bytes(b1))




    