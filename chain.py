import datetime as date
from block import Block


class Chain:
    def __init__(self):
        self.tail = self.create_genesis_block()
        self.blocks = [self.tail]

    def __str__(self):
        s = "  BLOCKCHAIN\n\n"
        for b in self.blocks:
            s += str(b) + "\n\n"
        return s

    def next_block(self, last_block, data):
        index = last_block.index + 1
        timestamp = date.datetime.now()
        hash = last_block.hash
        self.tail = Block(index, timestamp, data, hash)
        self.blocks.append(self.tail)
        return self

    @staticmethod
    def create_genesis_block():
        return Block(0, date.datetime.now(), "Genesis Block", "0")


if __name__ == "__main__":
    pass
