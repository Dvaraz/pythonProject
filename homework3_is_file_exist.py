import argparse
import pickle
import json
import os


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-filename", required=True, help="Enter file name for chek")
    return parser


if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args()
    a = os.getcwd()
    if os.path.isfile(a + "\\" + namespace.filename):
        with open(namespace.filename, "r") as f:
            b = json.load(f)
            print(b)
