from chain import Chain
import random
import string


def test():
    test_chain = Chain()
    test_num_blocks = 10

    for i in range(1, test_num_blocks + 1):
        token = "".join(random.choice(string.ascii_uppercase
                                      + string.ascii_lowercase + string.digits) for x in range(16))
        test_chain.next_block(test_chain.tail, token)

    print(test_chain)


if __name__ == "__main__":
    test()
