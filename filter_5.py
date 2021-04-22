def test(x , y):
    return tuple(str(x) + str(y))

def test_n(*args):
    return tuple(args)

if __name__ == '__main__':
    string_1 = "asx"
    string_2 = "bnm"
    string_3 = "qwe"
    int_1 = [1, 2, 3]
    int_2 = [4, 5, 6, 7]
    int_3 = [7, 8, 9]
    print(map(test, string_1, string_2))
    for _ in map(test, string_1, string_2):
        print(_)
    for _ in map(test, int_1, int_2):
        print(_)
    for _ in map(test_n, string_1, string_2, string_3):
        print(_)
    for _ in map(test_n, int_1, int_2, int_3):
        print(_)