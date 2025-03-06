import hashlib
import time

class Block:
  def __init__(self, transactions, timestamp, data, prior_hash=''):
    self.transactions = transactions
    self.timestamp = timestamp
    self.data = data
    self.prior_hash = prior_hash
    self.nonce = 0
    self.hash = self.create_hash()

  def create_hash(self):
    #Converting all properties into a string to encode them
    block_string = f"{self.transactions}{self.timestamp}{self.data}{self.prior_hash}{self.nonce}".encode()
    #Return the SHA-256 hash of the concatenated string
    return hashlib.sha256(block_string).hexdigest()

  def mine_block(self, difficulty):
    #Loop until the hash begins with required number of zeros
    while self.hash[:difficulty] != "0"*difficulty:
      self.nonce +=1
      self.hash = self.create_hash()
      print('Block Hash: '+self.hash)


class Transaction:
  def __init__(self, from_addr, to_addr, amount):
    self.from_addr = from_addr
    self.to_addr = to_addr
    self.amount = amount

class ArslanoBlockchain:

    def __init__(self):
      self.chain = [self.create_genesis_block()]
      self.difficulty = 2
      self.pending_transactions = []
      self.mining_reward = 5

    def create_genesis_block(self):
      return Block(0,21/11/2004,'BlockchainRevolution','0')

    def get_last_block(self):
      return self.chain[-1] # Return the last block to link it to the new one later:))

    def mine_pending_transactions(self, mining_reward_address):
      # Creating a new block with all pending transactions:
      block = Block(time.time(), self.pending_transactions, self.get_last_block().hash)
      block.mine_block(self.difficulty)

      # Adding the new block above to the chain
      self.chain.append(block)

      self.pending_transactions = [Transaction(None, mining_reward_address, self.mining_reward)]
import hashlib
import time

class Block:
  def __init__(self, transactions, timestamp, data, prior_hash=''):
    self.transactions = transactions
    self.timestamp = timestamp
    self.data = data
    self.prior_hash = prior_hash
    self.nonce = 0
    self.hash = self.create_hash()

  def create_hash(self):
    #Converting all properties into a string to encode them
    block_string = f"{self.transactions}{self.timestamp}{self.data}{self.prior_hash}{self.nonce}".encode()
    #Return the SHA-256 hash of the concatenated string
    return hashlib.sha256(block_string).hexdigest()

  def mine_block(self, difficulty):
    #Loop until the hash begins with required number of zeros
    while self.hash[:difficulty] != "0"*difficulty:
      self.nonce +=1
      self.hash = self.create_hash()
      print('Block Hash: '+self.hash)


class Transaction:
  def __init__(self, from_addr, to_addr, amount):
    self.from_addr = from_addr
    self.to_addr = to_addr
    self.amount = amount

class ArslanoBlockchain:

    def __init__(self):
      self.chain = [self.create_genesis_block()]
      self.difficulty = 2
      self.pending_transactions = []
      self.mining_reward = 5

    def create_genesis_block(self):
      return Block(0,21/11/2004,'BlockchainRevolution','0')

    def get_last_block(self):
      return self.chain[-1] # Return the last block to link it to the new one later:))

    def mine_pending_transactions(self, mining_reward_address):
      # Creating a new block with all pending transactions:
      block = Block(time.time(), self.pending_transactions, self.get_last_block().hash)
      block.mine_block(self.difficulty)

      # Adding the new block above to the chain
      self.chain.append(block)

      self.pending_transactions = [Transaction(None, mining_reward_address, self.mining_reward)]


    def create_transaction(self, transaction):
      self.pending_transactions.append(transaction)

    def get_balance_of_address(self, address):
      balance = 0

      for block in self.chain:
        for transaction in block.transaction:
          if transaction.from_addr == address:
            balance -= transaction.amount
          if transaction.to_addr == address:
            balance += transaction.amount

      return balance



   # def add_block(self, new_block):
    #  new_block.prior_hash = self.get_last_block().hash
     # new_block.hash = new_block.create_hash()
      #new_block.mine_block(self.difficulty)
     # self.chain.append(new_block)

    def is_bc_valid(self):
      for i in range(1, len(self.chain)):
        current_block = self.chain[i]
        previous_block = self.chain[i-1]

        # Check the hash
        if current_block.hash != current_block.create_hash():
          return False
        # Check if the prior hash is correct
        if current_block.prior_hash != previous_block.hash:
          return False

      return True

#arslano_coin = ArslanoBlockchain()

#arslano_coin.add_block(Block(1, '22/11/2004', 'amount = 1')) #this line and the two below were causing an error because add_block was commented out
#arslano_coin.add_block(Block(2, '23/11/2004', 'amount = 3'))
#arslano_coin.add_block(Block(3, '24/11/2004', 'amount = 5'))

#arslano_coin.create_transaction(Transaction("address1","address2",75))

#print("Is ArslanChain valid? " + str(arslano_coin.is_bc_valid()))

#arslano_coin.chain[2].data = "amount = 1 billion dollars"

#print("Is ArslanChain valid after the update? " + str(arslano_coin.is_bc_valid()))
#import json
#print(json.dumps(arslano_coin.chain, default=lambda o: o.__dict__, indent=4))




   # def add_block(self, new_block):
    #  new_block.prior_hash = self.get_last_block().hash
     # new_block.hash = new_block.create_hash()
      #new_block.mine_block(self.difficulty)
     # self.chain.append(new_block)

arslano_coin = ArslanoBlockchain()

## Creating new transactions
arslano_coin.create_transaction(Transaction('address1', 'address2', 75))
arslano_coin.create_transaction(Transaction('address2', 'address1', 25))


# Mine the pending transactions

print("Starting the mining process")
arslano_coin.mine_pending_transactions('miner-address')

#Check the balance
print(f"\nBalance of miner's wallet: {arslano_coin.get_balance_of_address('miner-address')}")

 #Mine again to receive the reward
print("Mining again to receive the reward...")
arslano_coin.mine_pending_transactions('miner-address')

# Check the balance of the miner again
print(f"\nBalance of miner's wallet after second mining: {arslano_coin.get_balance_of_address('miner-address')}")



# arslano_coin.add_block(Block(1, '22/11/2004', 'amount = 1'))
# arslano_coin.add_block(Block(2, '23/11/2004', 'amount = 3'))
# arslano_coin.add_block(Block(3, '24/11/2004', 'amount = 5'))

#arslano_coin.create_transaction(Transaction("address1","address2",75))

#print("Is ArslanChain valid? " + str(arslano_coin.is_bc_valid()))

#arslano_coin.chain[2].data = "amount = 1 billion dollars"

#print("Is ArslanChain valid after the update? " + str(arslano_coin.is_bc_valid()))
#import json
#print(json.dumps(arslano_coin.chain, default=lambda o: o.__dict__, indent=4))


