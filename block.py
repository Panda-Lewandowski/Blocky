import hashlib as hsh
import datetime as date

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.hash_block()

    def __str__(self):
        return "Block #" + str(self.index) + "   " + str(self.timestamp) + "\n" + "Data Hash: " + str(self.hash)

    def hash_block(self):
        d = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash)

        sha = hsh.sha256()
        sha.update(d.encode())

        return sha.hexdigest()


if __name__ == "__main__":
    pass
