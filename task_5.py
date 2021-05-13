import re
import json

BOOK_BODY_PATTERN = r"#{4}\s+?(?P<position>.{,2}).+?(?P<book>\[.+?\])(?P<book_url>\(.+?\))\s(?P<author>\w{2}\s+?.+?\s.+?)\s(?P<recommended>\(.+?\))\n+?!\[\](?P<cover_url>\(.+?\))\n+(?P<description>\".+?\")."
BOOKS_FILE = 'books.md'

# sorted("123", key=popularity)


def task_5():
    with open(BOOKS_FILE, "r") as f:
        pattern = re.compile(BOOK_BODY_PATTERN, re.DOTALL)
        a = pattern.search(f.read()).groupdict()
        for _ in a:
            print(_)
        # for match in pattern.finditer(f.read()):
        #     yield (match.groupdict())

task_5()

# if __name__ == '__main__':
#     pass
    # for _ in task_5():
    #     print(_)

    # with open("books.json", "w") as f:
    #     for _ in task_5():
    #         json.dump(_, f, indent=3)