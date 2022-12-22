import copy
from block import block

class blockchain:
    def __init__(self, initial_block):
        self.blocks = [initial_block] #stores the blockchain as a list

    def length(self):
        return len(self.blocks)

    #check block validity using parent hash and epoch
    def block_validity(self, block, prev_block, common_hash):
        #assert block is not genesis block
        assert block.parent != "-1", 'This is the genesis block!'
        hasher = common_hash.get_hasher()
        hasher.update(bytes(prev_block))
        assert block.parent == hasher.finalize() and block.epoch > prev_block.epoch, "Block is invaild!"

    #checks chain validity by checking block validity of each block in the chain
    def chain_validity(self):
        for index, block in enumerate(self.blocks[1:]):
            self.block_validity(block, self.blocks[index])

    #first checks the validity of the block and if the block is valid, it adds it to the block chain in the end
    def add_block(self, block, common_hash):
        self.block_validity(block, self.blocks[-1], common_hash)
        self.blocks.append(copy.deepcopy(block))

    #checks if the complete block chain is notarized. It does so by checking each block in the chain
    def is_notarized(self):
        for block in self.blocks:
            if not block.is_notarized():
                return False
            return True

    #returns the length of the current blockchain
    def length(self):
        return len(self.blocks)

        