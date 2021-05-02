def test_n(*args):
    return tuple(args)


def test(x, y):
    return tuple(str(x) + str(y))


def test_gen(x, y):
    max_len = max(x, y, key=len)
    if len(max_len) == len(x):
        right = True
    else:
        right = False
    for i in range(len(max_len)):
        try:
            yield tuple(str(x[0]) + str(y[0]))
            x = x[1:]
            y = y[1:]
        except IndexError:
            max_len = max(x, y, key=len)
            x = ""
            y = ""
            for i in range(len(max_len)):
                if right:
                    yield tuple(str(max_len[0] + "-"))
                else:
                    yield tuple(str("-" + max_len[0]))
                max_len = max_len[1:]

if __name__ == '__main__':
    string_1 = "asxccccaaa"
    string_2 = "bnmssssa"
    string_3 = "qwe"
    int_1 = [1, 2, 3]
    int_2 = [4, 5, 6, 7]
    int_3 = [7, 8, 9]

    print(max(string_1, string_2, key=len))
    print("#" * 20)
    a = test_gen(string_1, string_2)
    for _ in a:
        print(_)
