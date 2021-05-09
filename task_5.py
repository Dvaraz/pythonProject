import re

BOOK_BODY_PATTERN = r"#{4}\s+?(?P<position>.{,2}).+?(?P<book>\[.+?\])(?P<book_url>\(.+?\))\s(?P<author>\w{2}\s+?.+?\s.+?)\s(?P<recommended>\(.+?\))\n+?!\[\](?P<cover_url>\(.+?\))\n+(?P<description>\".+?\")."
BOOKS_FILE = 'books.md'

# sorted("123", key=popularity)

def task_5():
    with open(BOOKS_FILE, "r") as f:
        pattern = re.compile(BOOK_BODY_PATTERN, re.DOTALL)
        for match in pattern.finditer(f.read()):
            print(match.groupdict(), end="\n\n")
            # print(match["position"])


if __name__ == '__main__':
    print(task_5())