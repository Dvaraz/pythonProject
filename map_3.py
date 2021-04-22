from itertools import repeat

def round_2(x):
    return round(x, 2)

if __name__ == '__main__':

    my_floats = [
        4.356345,
        6.0934,
        3.245235,
        9.77545,
        2.164234234,
        8.884234235,
        4.595235346645
    ]
    print(list(map(round, my_floats, [2] * len(my_floats))))
    print(list(map(round, my_floats, repeat(2))))

    print([round(x, 2) for x in my_floats])
    print(list(map(lambda x: round(x, 2), my_floats)))