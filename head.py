import argparse


def createParser():
    pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("file_name", type=str, help="Name of file")
    parser.add_argument("-n", type=int, default=10, help="number of stings")
    namespace = parser.parse_args()
    with open(namespace.file_name, "r") as f:
        for _ in range(namespace.n):
            print(f.readline().strip())