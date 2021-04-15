import itertools
from string import ascii_lowercase
if __name__ == '__main__':
    print("Test")
    alphabet = ascii_lowercase
    for _ in zip(itertools.count(1), alphabet):
        print(_)