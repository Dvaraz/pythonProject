import itertools
from string import ascii_lowercase


def enumerate_(x, count = 0):
    return zip(itertools.count(count), x)


if __name__ == '__main__':
    print("Test")
    alphabet = ascii_lowercase
    a = enumerate_(alphabet, 1)

    for _ in a:
        print(_)