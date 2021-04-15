from itertools import repeat
from operator import index


def task_3(str_, list_index):
    return list(map(get_char, repeat(str_), list_index)) # to do operator index and list comprehension


def get_char(str_, index):
    return str_[index]

if __name__ == '__main__':
    string_ = "Всем привет"
    list_ = [1, 3, 5]

    print("".join(task_3(string_, list_)))


