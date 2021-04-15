from itertools import count


def count_sqrt(x):
    return x ** 2


def is_even(x):
    return x % 2 == 0


if __name__ == '__main__':
    a = filter(lambda x: x % 2 == 0, map(lambda x: x ** 2, count()))
    b = map(lambda x: x ** 2, count(0, 2))
    b_func = map(count_sqrt, count())
    a_func = filter(is_even, map(count_sqrt, count()))

    print("Func")
    for _ in range(10):
        print(next(a_func))

    print("lambda")
    for _ in range(10):
        print(next(a))

    for _ in range(10):
        print(next(b))