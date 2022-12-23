import time
import copy
from defaulthash import common_hash
from validator import validator
from block import block

#initialization
validator_count = 0
common_hash_ = common_hash()
validators = []
delta = 2

#simulation starts
genesis_block = block('-1', 0, [])
genesis_block.notarize()
genesis_block.finalize()

genesis_time = time.time()

v0 = validator(0, genesis_time, copy.deepcopy(genesis_block), common_hash_, delta)
v1 = validator(1, genesis_time, copy.deepcopy(genesis_block), common_hash_, delta)
v2 = validator(2, genesis_time, copy.deepcopy(genesis_block), common_hash_, delta)

validators = [v0, v1, v2] 
validator_count = len(validators)

##ROUND 1
#sleep for a while
time.sleep(10)


#add transactions
txs0 = "transaction 0"
txs1 = "transaction 1"
txs2 = "transaction 2"
v0.add_transaction(txs0)
v0.broadcast_transaction([v1, v2], txs0)
v1.add_transaction(txs1)
v1.broadcast_transaction([v0, v2], txs1)
v2.add_transaction(txs2)
v2.broadcast_transaction([v0, v1], txs2)

#test transactions
transactions = [txs0, txs1, txs2]
assert v0.get_unconfirmed_transactions() == transactions, "transactions don't match"
assert v1.get_unconfirmed_transactions() == transactions, "transactions don't match"
assert v2.get_unconfirmed_transactions() == transactions, "transactions don't match"


#leader proposes block
leader_public_key = None
proposal = None
for v in validators:
    if v.is_epoch_leader(validator_count):
        leader_public_key, proposal = v.propose_block()
        break
proposal.print_()

#send the proposed block to all other validators and voting beings

votes = []
for v in validators:
    votes.append(v.voting_proposed_block(leader_public_key, proposal, validator_count))


#broadcast votes
for v in validators:
    for i in range(len(votes)):
        v.vote_receive(validators[i].get_public_key(), votes[i], validator_count)

#print blockchains
for v in validators:
    print(v.id)
    print(v.final_blockchain)
    print(v.validator_blockchains)


##ROUND 2
#sleep for a while
time.sleep(10)

#add transactions
txs4 = "transaction 4"
txs5 = "transaction 5"
txs6 = "transaction 6"
v0.add_transaction(txs4)
v0.broadcast_transaction([v1, v2], txs4)
v1.add_transaction(txs5)
v1.broadcast_transaction([v0, v2], txs5)
v2.add_transaction(txs6)
v2.broadcast_transaction([v0, v1], txs6)


#check if transactions match
transactions = [txs4, txs5, txs6]
assert v0.get_unconfirmed_transactions() == transactions, "transactions don't match"
assert v1.get_unconfirmed_transactions() == transactions, "transactions don't match"
assert v2.get_unconfirmed_transactions() == transactions, "transactions don't match"


#leader proposes block
leader_public_key = None
proposal = None
for v in validators:
    if v.is_epoch_leader(validator_count):
        leader_public_key, proposal = v.propose_block()
        break

proposal.print_()

#send the proposed block to all other validators and voting beings
votes = []
for v in validators:
    votes.append(v.voting_proposed_block(leader_public_key, proposal, validator_count))


#broadcast votes
for v in validators:
    for i in range(len(votes)):
        v.vote_receive(validators[i].get_public_key(), votes[i], validator_count)

#print blockchains
for v in validators:
    print(v.id)
    print(v.final_blockchain)
    print(v.validator_blockchains)



##ROUND 3
#sleep for a while
time.sleep(10)

#add transactions
txs7 = "transaction 7"
txs8 = "transaction 8"
txs9 = "transaction 9"
v0.add_transaction(txs7)
v0.broadcast_transaction([v1, v2], txs7)
v1.add_transaction(txs8)
v1.broadcast_transaction([v0, v2], txs8)
v2.add_transaction(txs9)
v2.broadcast_transaction([v0, v1], txs9)


#check if transactions match
transactions = [txs7, txs8, txs9]
assert v0.get_unconfirmed_transactions() == transactions, "transactions don't match"
assert v1.get_unconfirmed_transactions() == transactions, "transactions don't match"
#assert v2.get_unconfirmed_transactions() == transactions, "transactions don't match"


#leader proposes block
leader_public_key = None
proposal = None
for v in validators:
    if v.is_epoch_leader(validator_count):
        leader_public_key, proposal = v.propose_block()
        break

proposal.print_()

#send the proposed block to all other validators and voting beings
votes = []
#Byzantine behavior#
for v in validators[:-1]:
    votes.append(v.voting_proposed_block(leader_public_key, proposal, validator_count))


#broadcast votes
for v in validators:
    for i in range(len(votes)):
        v.vote_receive(validators[i].get_public_key(), votes[i], validator_count)

#print blockchains
for v in validators:
    print("validator id: ", v.id)
    v.final_blockchain.print_chain()
    #print(v.validator_blockchains)

print("Final Chain of v0 matches v1: ", v0.isequal(v1))
print("Final Chain of v1 matches v2: ", v1.isequal(v2))
print("Final Chain of v0 matches v2: ", v0.isequal(v2))

# print("Length of final chain: ", v0.final_chain().length())