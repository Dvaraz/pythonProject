
if __name__ == '__main__':
    num_list = [
        "12",
        "14",
        3.1415926,
        5,
        0xFF,
        0b1010101010
    ]

    print(tuple(map(int, num_list)))
    print(list(map(lambda x: int(x), num_list)))
    print([int(x) for x in num_list])
