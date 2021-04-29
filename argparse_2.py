import argparse


def createParser():
    pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("file_name", type=str, help="Name of file")
    namespace = parser.parse_args()
    with open(namespace.file_name, "r") as f:
        number_of_lines = 0
        for line in f:
            number_of_lines += 1
        print(number_of_lines) 