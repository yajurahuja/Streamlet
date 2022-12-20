class validator:
    def __init__(self, id, genesis_time, init_block):
        self.id = id
        self.genesis_time = genesis_time
        self.keypair = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        self.final_blockchain = blockchain(init_block)
        self.validator_blockchains = []
        self.new_transactions = []

    def output(self):
        self.final_blockchain
    
    def add_transaction(self, transaction):
        self.new_transactions.append(transactions)

    def broadcast_transactions(self, validators, transaction):
        for validator in validators:
            validator.add_transaction(transaction)

    def get_current_epoch(self, delta):
        #TODO: fix time passing reference
        return self.genesis_time / (2 * delta)

    def is_epoch_leader(self, validator_count):
        retunn self.id == self.get_epoch_leader(validator_count)

    def get_new_transactions(self):
        new_transactions = copy.deepcopy(self.new_transactions)
        for blockchain in self.validator_blockchains:
            for block  in blockchain.blocks:
                for transaction in block.txs:
                    if transaction in new_transactions:
                        index = new_transactions.index(transaction)
                        new_transactions.remove(index)

        return new_transactions

    def propose_block(self):
        epoch = self.get_current_epoch()
        longest_notarized_chain = self.get_longest_notarized_chain()
        #TODO: hashing of the data
        new_transactions = self.get_new_transactions()
        parent_hash = ""
        proposed_block = block(parent_hash, epoch, new_transactions)
        signer = None
        signed_block = None
        return signed_block

    def receive_proposed_block(self, leader_public_key, vote, node_count):
        #TODO: 
        assert self.get_epoch_leader(node_count) == vote.id, "Vote ID doesn't match"
        Verifier = 


    def can_extend_notarized_blockchain(self, blockchain):
        for block in blockchain.blocks[:-1]:
            if not block.meta_data.is_notarized():
                return False
        return True

    def find_blockchain_index(self, block):
        h = None #TODO: Create Hasher 
        for index, blockchain in enumerate(self.validator_blockchains):
            last_block = blockchain.blocks[-1]
            
    def find_block(self, vote_block):
        for index, blockchain in enumerate(self.validator_blockchains):
            for block in blockchain.blocks.reverse():
                if block == vote_block:
                    return (block, index)
        
        for block in self.final_blockchain.blocks.reverse():
            if vote_block == block:
                return (block, -1)

        return None

    def find_longest_finalized_chain(self):
        longest_notarized_chain = self.final_blockchain
        length = 0
        for blockchain in self.validator_blockchains:
            if blockchain.is_notarized() and len(blockchain.blocks) > length:
                longest_notarized_chain = blockchain
                length = len(blockchain.blocks)
        return longest_notarized_chain

    def receive_vote(self, public_key, vote, count):


    def finalize_blockchain(self, bc)
    {
        blockchain = None
        if bc == -1:
            blockchain = self.final_blockchain
        else:
            blockchain = self.validator_blockchains[bc]
        notarized = 0
        if blockchain.length() > 2:
            for block in blockchain.blocks():
                if block.meta_data.is_notarized():
                    notarized += 1
                else:
                    break
        if notarized > 2:
            finalized_blocks = []
            for block in blockchain.blocks[:notarized]:
                block.meta_data.finalized = True
                finalized_blocks.append(copy.deepcopy(block))
                for transactions in block.txs:

            



    }
    



