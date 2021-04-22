if __name__ == '__main__':
    matrix = """
    1 2 3
    4 5 6
    7 8 9
    10 11 12
    """
    list_1 = [int(x) for x in matrix.split()]
    # list_1 = list(map(int, matrix.split()))
    list_1 = [list_1[:3]] + [list_1[3:6]] + [list_1[6:9]] + [list_1[9:12]]
    print(list_1)