from operator import add

if __name__ == '__main__':
    list_1 = [1, 2, 3]
    list_2 = [4, 5, 6]

    print(list(map(sum, zip(list_1, list_2))))

    print(list(map(add, list_1, list_2)))

    print(list(map(lambda x, y: x + y, list_1, list_2)))