# ArslanoBlockchain

A simple blockchain implementation in Python that demonstrates the core concepts of blockchain technology including blocks, transactions, mining, and proof of work.

## Overview

ArslanoBlockchain is a lightweight blockchain implementation that includes:

- Block creation and mining with proof-of-work
- Transaction handling
- Blockchain validation
- Mining rewards
- Wallet balance tracking

This project serves as an educational tool to understand the fundamental concepts behind blockchain technology.

## Features

- **Proof of Work**: Implements a mining system requiring computational work to validate blocks
- **Transactions**: Supports simple transactions between addresses
- **Mining Rewards**: Miners receive rewards for successfully mining blocks
- **Chain Validation**: Verifies the integrity of the entire blockchain
- **Balance Tracking**: Keeps track of address balances based on transaction history

## Components

### Block

The `Block` class represents individual blocks in the blockchain. Each block contains:

- Transactions
- Timestamp
- Data payload
- Hash of the previous block
- Nonce for proof-of-work
- Its own hash

```python
class Block:
  def __init__(self, transactions, timestamp, data, prior_hash=''):
    self.transactions = transactions
    self.timestamp = timestamp
    self.data = data
    self.prior_hash = prior_hash
    self.nonce = 0
    self.hash = self.create_hash()
```

### Transaction

The `Transaction` class represents value transfers between addresses:

```python
class Transaction:
  def __init__(self, from_addr, to_addr, amount):
    self.from_addr = from_addr
    self.to_addr = to_addr
    self.amount = amount
```

### ArslanoBlockchain

The main blockchain class that manages:

- The chain of blocks
- Pending transactions
- Mining difficulty
- Mining rewards

## Usage Example

```python
# Create a new blockchain instance
arslano_coin = ArslanoBlockchain()

# Create transactions
arslano_coin.create_transaction(Transaction('address1', 'address2', 75))
arslano_coin.create_transaction(Transaction('address2', 'address1', 25))

# Mine pending transactions (this will include the transactions in a new block)
print("Starting the mining process")
arslano_coin.mine_pending_transactions('miner-address')

# Check the balance of the miner
print(f"\nBalance of miner's wallet: {arslano_coin.get_balance_of_address('miner-address')}")

# Mine again to receive the reward from the previous mining operation
print("Mining again to receive the reward...")
arslano_coin.mine_pending_transactions('miner-address')

# Check the miner's balance again
print(f"\nBalance of miner's wallet after second mining: {arslano_coin.get_balance_of_address('miner-address')}")
```

## Implementation Details

### Block Mining

The `mine_block` method in the `Block` class implements proof-of-work by finding a hash that starts with a specified number of zeros:

```python
def mine_block(self, difficulty):
  while self.hash[:difficulty] != "0"*difficulty:
    self.nonce += 1
    self.hash = self.create_hash()
    print('Block Hash: '+self.hash)
```

### Blockchain Validation

The blockchain validates its integrity by:
1. Verifying each block's hash
2. Ensuring each block properly references the previous block's hash

```python
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
```

## Known Issues

- The `create_genesis_block()` method has a date format issue (21/11/2004 should be formatted properly)
- There's a potential bug in the `mine_pending_transactions` method where the `Block` constructor arguments aren't in the correct order
- The `get_balance_of_address` method tries to access `block.transaction` but it should be `block.transactions`

## Future Enhancements

- Add public/private key cryptography for transaction signing
- Implement a peer-to-peer network for distributed consensus
- Add a mechanism for adjusting difficulty based on mining rate
- Create a simple API interface

## License

This project is available as an educational resource.

## Credits

Developed as a demonstration blockchain implementation.
