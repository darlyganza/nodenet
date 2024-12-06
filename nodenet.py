import hashlib
import time

# Definition of the Block class
class Block:
    def __init__(self, position, prev_block_hash, timestamp, transactions):
        self.index = position  # Block's position in the chain
        self.prev_hash = prev_block_hash  # Hash of the previous block
        self.timestamp = timestamp  # Creation time of the block
        self.transactions = transactions  # Data contained in the block
        self.nonce = 0  # Counter for Proof of Work
        self.current_block_hash = self.calculate_hash()  # Calculate the hash of the block

    def calculate_hash(self):
        # Create a string representation of the block's attributes
        hash_representation = f"{self.index}{self.prev_hash}{self.timestamp}{self.transactions}{self.nonce}"
        return hashlib.sha256(hash_representation.encode()).hexdigest()

# Definition of the Blockchain class
class Blockchain:
    def __init__(self):
        self.chain = []  # Initialize the blockchain as an empty list
        self.create_genesis_block()

    def create_genesis_block(self):
        # Genesis block creation with no previous hash
        genesis_block = Block(0, "0", time.time(), "Genesis Block")
        self.chain.append(genesis_block)

    def add_block(self, transactions, difficulty=4):
        previous_block = self.chain[-1]
        index = previous_block.index + 1
        timestamp = time.time()
        new_block = Block(index, previous_block.current_block_hash, timestamp, transactions)
        self.proof_of_work(new_block, difficulty)
        self.chain.append(new_block)

    def proof_of_work(self, block, difficulty):
        # Perform Proof of Work by finding a hash with the required number of leading zeros
        prefix = '0' * difficulty
        while not block.current_block_hash.startswith(prefix):
            block.nonce += 1
            block.current_block_hash = block.calculate_hash()

    def print_chain(self):
        # Print all blocks in the blockchain
        for block in self.chain:
            print(f"Block Index: {block.index}")
            print(f"Time: {block.timestamp}")
            print(f"Previous Hash: {block.prev_hash}")
            print(f"Current Hash: {block.current_block_hash}")
            print(f"Nonce: {block.nonce}")
            print(f"Transaction: {block.transactions}")
            print("_" * 25)
# printing out the blockchain to test functionality
if __name__ == "__main__":
    blockchain = Blockchain()  # Create a new blockchain
    blockchain.add_block("Transaction 1")  # Add the first block
    blockchain.add_block("Transaction 2")  # Add the second block
    blockchain.add_block("Transaction 3")  # Add the third block
    blockchain.print_chain()  # Print the entire blockchain
