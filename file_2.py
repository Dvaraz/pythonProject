FILENAME = "test.txt"


def read_text_file(filename):
    with open(filename, "r") as f:
        for line in f:
            print(line.strip())   # or print(line, end="")


def read_bin_file(filename):
    with open(filename, "rb") as f:
        print(f.read())


def text_to_bin(filename):
    with open(filename, "rb") as src_file:
            with open(filename + "_bin", "wb") as dst_file:
                for line in src_file:
                    dst_file.write(line)


if __name__ == '__main__':
    # read_text_file(FILENAME)
    # read_bin_file(FILENAME)
    text_to_bin(FILENAME)