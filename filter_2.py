import random


if __name__ == '__main__':

    n = 100
    random_list = [random.randint(-100, 100) for _ in range(n)]

    print(sorted(list(filter(lambda x: x % 3 == 0 and x < 0, random_list))))