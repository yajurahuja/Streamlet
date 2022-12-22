#this is the first simulation and test case
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

txs0 = "transaction 0"
txs1 = "transaction 1"
txs2 = "transaction 2"

#sleep for a while
time.sleep(5)

#add transactions
v0.add_transaction(txs0)
v0.broadcast_transaction([v1, v2], txs0)
v1.add_transaction(txs1)
v1.broadcast_transaction([v0, v2], txs1)
v2.add_transaction(txs2)
v2.broadcast_transaction([v0, v1], txs2)

#test transactions
transactions = ['transaction 0', 'transaction 1', 'transaction 2']
assert v0.new_transactions == transactions, "transactions don't match"
assert v1.new_transactions == transactions, "transactions don't match"
assert v2.new_transactions == transactions, "transactions don't match"


leader_public_key = None
block = None
for v in validators:
    if v.is_epoch_leader(validator_count):
        leader_public_key, block = v.propose_block()

block.print_()

