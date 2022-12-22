from meta_data import meta_data
import copy
class block:
    def __init__(self, parent, epoch, txs):
        self.parent = parent #stores the parent hash
        self.epoch = epoch #current epoch number
        self.txs = txs #list of transactions
        self.meta_data = meta_data() #any meta data to store 


    def print_(self):
        print("Epoch: ", self.epoch)
        print("txs: ", self.txs)
        #print("parent sig: ", self.parent)

    #returns the instance string in the bytes format when the bytes() function is called
    def __bytes__(self):
        sig_str = "{} {} {}".format(self.parent, self.epoch, self.txs)
        return bytes(sig_str, 'utf-8')

    #signature encoding is similar to the bytes format output
    def signature_encode(self):
        #TODO
        sig_str = "{} {} {}".format(self.parent, self.epoch, self.txs)
        print(sig_str)
        signature = bytes(sig_str, 'utf-8')
        print(signature)
        return signature

    #it compares all the transactions in the the transaction lists
    def compare_txs(self, other_txs):
        return self.txs == other_txs

    #checks if the self block and the other block have equal entries. We use this instead of direct instance comparison
    def isequal(self, other):
        return self.parent == other.parent and self.epoch == other.epoch and self.compare_txs(other.txs)

    #gets the hash value of the block
    def get_hash(self, common_hash):
        h = common_hash.get_hasher()
        h.update(bytes(self))
        return h.finalize()

    #check if the vote already exists in the vote list
    def check_vote(self, vote):
        self.meta_data.check_vote(vote)

    #adds the vote to the vote list of the block
    def add_vote(self, vote):
        self.meta_data.votes.append(vote)

    #gets the vote count for the block
    def get_vote_count(self):
        return len(self.meta_data.votes)

    #sets the notarized block flag to true
    def notarize(self):
        self.meta_data.notarized = True

    #returns if the block has been noterized
    def is_notarized(self):
        return self.meta_data.is_notarized()

    def finalize(self):
        self.meta_data.finalized = True
    
    def is_finalized(self):
        return self.meta_data.finalized

# if __name__ == "__main__":
    # b1 = block("123", 1, ["hey", "hello", "how are you"])
    # b2 = block("123", 1, ["hey", "hello", "how are you"])
    # b3 = copy.deepcopy(b2)
    # print(bytes(b1))




    