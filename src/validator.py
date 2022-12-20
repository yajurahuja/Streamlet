class validator:
    def __init__(self, id, genesis_time, init_block, common_hash):
        self.id = id
        self.genesis_time = genesis_time
        self.key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
        self.final_blockchain = blockchain(init_block)
        self.validator_blockchains = []
        self.new_transactions = []
        self.hash = common_hash

    
    #signature functions

    #signs a message/block and returns the signature
    self.sign(self, message):
        signature = self.key.sign(message,padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH), hashes.SHA256())
        return signature

    #get the public key fom the private key: key
    self.get_public_key(self):
        return self.key.public_key()

    #verifies the message using the publick key and the signature
    self.verify_signature(self, signature, message, public_key):
        public_key.verify(signature, message, padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH), hashes.SHA256())
        return True

    #returns the finalized blockchain
    def output(self):
        self.final_blockchain
    
    #adds a transaction to the unconfired transaction list
    def add_transaction(self, transaction):
        self.new_transactions.append(transactions)

    #broadcasts a transaction to all the validators
    def broadcast_transaction(self, validators, transaction):
        for validator in validators:
            validator.add_transaction(copy.deepcopy(transaction))

    #TODO
    #returns the current epoch
    def get_current_epoch(self, delta):
        #TODO: fix time passing reference
        return self.genesis_time / (2 * delta)

    #returns the selected leader for the current epoch
    def epoch_leader(self, numberValidators):
        epoch = self.get_current_epoch()
        hasher = self.hash.get_hasher()
        hasher.update(str(epoch))
        return hasher.finalize() % numberValidators

    #checks if the validator is the current epoch leader
    def is_epoch_leader(self, validator_count):
        retunn self.id == self.get_epoch_leader(validator_count)

   #returns the set of transactions not present in any blockchain
    def get_unconfirmed_transactions(self):
        txs = copy.deepcopy(self.new_transactions)
        for blockchain in self.validator_blockchains:
            for block in blockchain.blocks:
                for transaction in block.txs:
                    if transaction in txs: #remove transactions if already confirmed in prev blocks
                        txs.remove(transaction)

        return txs

    #returns the longest of the validator blockchains which has been notaized
    def longest_notarized_chain(self):
        longest_chain = self.final_blockchain
        length = 0
        for chain in self.validator_blockchains:
            if chain.is_notarized() and chain.length() > length:
                longest_chain = chain
                length = chain.length()
        return longest_chain

    #leader function
    #as the leader propose a block to be added to the blockchain
    def propose_block(self):
        longest_notarized_chain = self.longest_notarized_chain()
        proposed_block = block(longest_notarized_chain[-1].get_hash(self.hash), self.get_current_epoch(),  self.get_unconfirmed_transactions())
        signature = self.sign(bytes(proposed_block)) #sign the proposed block
        return (self.get_public_key(), vote(signature, proposed_block, self.id)) #send the block proposal as a vote

    #validator receives a block proposal, verifies the proposal and votes
    def voting_proposed_block(self, leader_public_key, vote, node_count):
        assert self.get_epoch_leader(node_count) == vote.id, "Vote ID doesn't match"
        self.verify_signature(self, vote.signature, bytes(vote.block), leader_public_key)
        return self.vote_for(vote.block)

    #validator vote function
    def vote_for(self, block):
        index = self.get_blockchain(block)
        current_chain = None
        #case where no block is found
        if index == -1:
            current_chain = blockchain(copy.deepcopy(block))
            self.validator_blockchains.append(current_chain)
        else:
            self.validator_blockchains[index].add_block(copy.deepcopy(block))
            current_chain = self.validator_blockchains[index]

        Vote = None
        if self.is_blockchain_notarized(current_chain):
            new_block = copy.deepcopy(block)
            signature = self.sign(bytes(new_block))
            Vote = vote(signature, new_block, self.id)
        return Vote


    #verifies of the blockchain is notarized without the last block
    def is_blockchain_notarized(self, blockchain):
        for block in blockchain.blocks[:-1]:
            if not block.is_notarized():
                return False
        return True

    #returns the blockchain whose tip is the given block 
    def get_blockchain(self, block):
        for index, blockchain in enumerate(self.validator_blockchains):
            chain_tip = blockchain.blocks[-1]
            if block.parent == chain_tip.get_hash(self.hash) and block.epoch > chain_tip.epoch:
                return index
        chain_tip = self.final_blockchain.blocks[-1]
        if not (chain_tip.get_hash(self.hash) == block.parent and block.epoch > chain_tip.epoch):
            print("get blockchain_index error")
            return -1
            

    #find the chain in which the block lies
    def find_block(self, vote_block):
        for index, blockchain in enumerate(self.validator_blockchains):
            for block in blockchain.blocks.reverse():
                if vote_block.isequal(block):
                    return (block, index)
        
        for block in self.final_blockchain.blocks.reverse():
            if vote_block.isequal(block):
                return (block, -1)

        return None

    #leader functionality
    #add votes received by the leader to the corresponding block
    def vote_receive(self, public_key, vote, validator_count):
        self.verify_signature(vote.signature,  bytes(vote.block), public_key)
        ret = self.find_block(vote.block)
        if ret == None:
            print("Block not found!")
        else: 
            block, index = ret
            if not block.check_vote(vote):
                block.add_vote(copy.deepcopy(vote))

            if block.is_notarized() and block.get_vote_count() > (2 * validator_count / 3):
                block.notarize()
                self.finalize_blockchain(self, index)
        return
        
            
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
            for block in blockchain.blocks:
                if block.is_notarized():
                    notarized += 1
                else:
                    break
            if notarized > 2:
                finalized_blocks = []
                for block in blockchain.blocks[:notarized]:
                    block.finalize()
                    finalized_blocks.add_block(copy.deepcopy(block))
                    for transaction in block.txs:
                        if transaction in self.new_transactions:
                            self.new_transactions.remove(transaction)
                blockchain.blocks = blockchain.blocks[:notarized]
                for block in finalized_blocks:
                    self.final_blockchain.blocks.add_block(copy.deepcopy(block))
                tip = self.final_blockchain[-1]

                tip_hash = tip.get_hash(self.hash)
                remove_chains = []
                for index, chains in enumerate(self.validator_blockchains):
                    if blockchain.blocks[0].parent == tip_hash and blockchain.blocks[0].epoch > tip.epoch:
                        retain_chains.append(index)
                updated_validator_blockchains = []
                for i in retain_chains:
                    updated_validator_blockchains.append(self.validator_blockchains[i])
                self.validator_blockchains = updated_validator_blockchains 
    }


