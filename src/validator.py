class validator:
    def __init__(self, id, genesis_time, init_block, common_hash):
        self.id = id
        self.genesis_time = genesis_time
        self.key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        self.final_blockchain = blockchain(init_block)
        self.validator_blockchains = []
        self.new_transactions = []
        self.hash = common_hash

    #DONE
    #signature functions
    self.sign(self, message):
        signature = self.key.sign(message,padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH), hashes.SHA256())
        return signature

    #DONE
    self.get_public_key(self):
        return self.key.public_key()

    #DONE
    self.verify_signature(self, signature, message, public_key):
        public_key.verify(signature, message, padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH), hashes.SHA256())
        return True

    #DONE
    def output(self):
        self.final_blockchain
    
    #DONE
    def add_transaction(self, transaction):
        self.new_transactions.append(transactions)

    #DONE
    def broadcast_transactions(self, validators, transaction):
        for validator in validators:
            validator.add_transaction(copy.deepcopy(transaction))

    #TODO
    def get_current_epoch(self, delta):
        #TODO: fix time passing reference
        return self.genesis_time / (2 * delta)

    #DONE
    def epoch_leader(self, numberValidators):
        epoch = self.get_current_epoch()
        hasher = self.common_hash.get_hasher()
        hasher.update(str(epoch))
        return hasher.finalize() % numberValidators

    #DONE
    def is_epoch_leader(self, validator_count):
        retunn self.id == self.get_epoch_leader(validator_count)

    #DONE
    def get_unconfirmed_transactions(self):
        txs = copy.deepcopy(self.new_transactions)
        for blockchain in self.validator_blockchains:
            for block in blockchain.blocks:
                for transaction in block.txs:
                    if transaction in txs: #remove transactions if already confirmed in prev blocks
                        index = new_transactions.index(transaction)
                        txs_transactions.remove(index)

        return new_transactions

    #DONE
    #leader function
    def block_proposal(self):
        longest_notarized_chain = self.get_longest_notarized_chain()
        proposed_block = block(str(hasher.finalize()),self.get_current_epoch(),  self.get_new_transactions())
        signature = self.sign(bytes(proposed_block))
        return (self.get_public_key(), Vote(signature, proposed_block, self.id))

    #DONE
    def receive_proposed_block(self, leader_public_key, vote, node_count):
        #TODO: 
        assert self.get_epoch_leader(node_count) == vote.id, "Vote ID doesn't match"
        self.verify_signature(self, vote.signature, bytes(vote.block), leader_public_key)
        return self.vote(vote.block)

    #DONE
    def vote(self, block):
        index = self.get_blockchain_index(block)
        current_chain = None
        #if block not found
        if index == -1:
            current_chain = blockchain(copy.deepcopy(block))
            self.validator_blockchains.append(current_chain)
        else:
            current_chain = self.validator_blockchains[index]
        
        Vote = None
        if self.is_blockchain_notarized(current_chain):
            new_block = copy.deepcopy(block)
            signature = self.sign(bytes(new_block))
            Vote = vote(signature, new_block, self.id)
        return Vote


    #DONE
    def is_blockchain_notarized(self, blockchain):
        for block in blockchain.blocks[:-1]:
            if not block.meta_data.is_notarized():
                return False
        return True

    #DONE
    def get_blockchain_index(self, block):
        for index, blockchain in enumerate(self.validator_blockchains):
            chain_tip = blockchain.blocks[-1]
            if block.parent == chain_tip.get_hash(self.common_hash) and block.epoch > chain_tip.epoch:
                return index
        chain_tip = self.final_blockchain.blocks[-1]
        if not (last_block.get_hash(self.common_hash) == block.parent and block.epoch > chain_tip.epoch):
            print("get blockchain_index error")
            return -1
            

    #DONE
    def find_block(self, vote_block):
        for index, blockchain in enumerate(self.validator_blockchains):
            for block in blockchain.blocks.reverse():
                if block == vote_block:
                    return (block, index)
        
        for block in self.final_blockchain.blocks.reverse():
            if vote_block == block:
                return (block, -1)

        return None


    #DONE
    def find_longest_finalized_chain(self):
        longest_notarized_chain = self.final_blockchain
        length = 0
        for blockchain in self.validator_blockchains:
            if blockchain.is_notarized() and blockchain.length() > length:
                longest_notarized_chain = blockchain
                length = blockchain.length()
        return longest_notarized_chain

    def vote(self, public_key, proposed_block, count_validators):
        
        #TODO: create verifier fro m public key
        #and verify vote
        assert 
        block = self.find_block(vote.block)
        if block == None:
            print("Unknown Block!")
        self.vote_for(proposed_block)

    

    #DONE
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
                for transaction in block.txs:
                    if transaction in self.new_transactions:
                        index = self.new_transactions.find(transaction)
                        self.new_transactions.remove(index)
            blockchain.blocks = blockchain.blocks[:notarized]
            for block in finalized_blocks:
                self.final_blockchain.blocks.append(copy.deepcopy(block))
            hasher = self.common_hash.get_hasher()
            tip = self.final_blockchain[-1]
            hasher.update(bytes(tip))
            tip_hash = str(hasher.finalize())
    }


