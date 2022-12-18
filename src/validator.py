class validator:
    def __init__(self, id, genesis_time, init_block):
        self.id = id
        self.genesis_time = genesis_time
        self.keypair = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        self.canonical_blockchain = blockchain(init_block)
        self.validator_blockchains = []
        self.new_transactions = []

    def output(self):
        self.canonical_blockchain
    
    def add_transaction(self, transaction):
        self.new_transactions.append(transactions)

    def broadcast_transactions(self, validators, transaction):
        for validator in validators:
            validator.add_transaction(transaction)

    def get_current_epoch(self, delta):
        #TODO: fix time passing reference
        return self.genesis_time / (2 * delta)

    def is_epoch_leader(self, validator_count):
        leader = self.get_epoch_leader(validator_count)
        self.id = leader

    def get_new_transactions(self):
        #TODO
        return False

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
        


    def can_extend_notarized_blockchain(self, blockchain):
        for block in blockchain.blocks[:-1]:
            if not block.meta_data.is_notarized():
                return False
        return True

    def find_blockchain_index(self, block):
        h = None#TODO: Create Hasher 
        for index, blockchain in enumerate(self.validator_blockchains):
            last_block = blockchain.blocks[-1]
            


