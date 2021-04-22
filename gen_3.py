def pairwise(iterable):
    # for i in range(len(iterable) - 1): # to do
    # yield [(iterable[i], iterable[i+1]) for i in range(len(iterable) - 1)]
    yield ((iterable[i], iterable[i + 1]) for i in range(len(iterable) - 1))


if __name__ == '__main__':
    a = pairwise([1, 2, 3, 4])
    for _ in a:
        for _ in _:
            print(_)

    # pts = pairwise([
    #         (3, 4),
    #         (4.5, 3),
    #         (2.1, -1),
    #         (6.8, -3),
    #         (1.4, 2.9)
    #     ])
    #
    # for _ in pts:
    #     print(_)