if __name__ == '__main__':
    list_1 = [
        [2, 3, 5, 7],
        [11, 13, 17, 19],
        [23, 29],
        [31, 37]
    ]

    print(list(map(len, list_1)))
    print(sum((list(map(len, list_1)))))
    print(max(map(sum, list_1)))