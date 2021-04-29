FILENAME = "test.txt"
# https://www.notion.so/3-3fe79a24f03045b8b27cca65ed6fa05c

def create_file(filename):
    with open(filename, "w", encoding="utf-8") as f:
        while True:
            input_ = input("Enter string or exit for exit: ")
            if input_ == "exit":
                break
            else:
                f.write(input_ + "\n")
                f.flush()   # f.flush() if want to save file right now.


def append_to_file(filename):
    with open(filename, "a", encoding="utf-8") as f:
        while True:
            input_ = input("Enter string or exit for exit: ")
            if input_ == "exit":
                break
            else:
                f.write(input_ + "\n")
                f.flush()   # f.flush() if want to save file right now.


if __name__ == '__main__':
    # create_file(FILENAME)
    append_to_file(FILENAME)