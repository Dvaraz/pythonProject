from task_1 import task_1
import re


def task_2():
    list_first_words = task_1()
    two_char_pattern = r".."

    # for i in list_first_words:
    #     print(i[:2])

    match_list = [re.search(two_char_pattern, word) for word in list_first_words]
    return [match.group() if match is not None else match for match in match_list]


if __name__ == '__main__':
    print(task_2())