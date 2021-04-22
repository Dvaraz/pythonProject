def count(start=1, step=1):
    current_num = start
    while True:
        yield current_num
        current_num += step


if __name__ == '__main__':
    counter = count()


    print(next(counter))
    print(next(counter))
    print(next(counter))



