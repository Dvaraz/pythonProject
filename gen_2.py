from random import choice
from string import ascii_letters, digits
# to do use alphabet


def password(symbols, n=8):
    symbols = list(map(str, symbols))
    while True:
        yield "".join((choice(symbols) for _ in range(n)))


if __name__ == '__main__':

    a = password(range(9))
    for _ in range(10):
        print(next(a))

    b = password(ascii_letters + digits)
    for _ in range(10):
        print(next(b))