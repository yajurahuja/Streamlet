import copy

class blockchain:
    def __init__(self, initial_block):
        self.blocks = [initial_block]

    def length(self):
        return len(self.blocks)

    def block_validity(self, block, prev_block, hasher):
        #assert block is not genesis block
        assert block.parent != "-1", 'This is the genesis block!'
        hasher.update(bytes(prev_block))
        assert block.parent == hasher.finalize() and block.epoch > prev_block.epoch, "Block is invaild!"

    def chain_validity(self):
        for index, block in enumerate(self.blocks[1:]):
            self.block_validity(block, self.blocks[index])

    def add_block(self):
        self.block_validity(block, self.blocks[-1])
        self.blocks.append(copy.deepcopy(block))

    def is_notarized(self):
        for block in self.blocks:
            if not block.meta_data.is_notarized():
                return False
            return True

        