import argparse
import pickle
import json


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("-filename", required=True, help="Enter file name for converting from json to pickle")
    return parser


def from_json_to_pickle(filename):
    with open(filename, "rb") as f:
        json_file = json.load(f)
        with open(filename + ".pickle", "wb") as f_pickle:
            pickle.dump(json_file, f_pickle)


if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args()
    from_json_to_pickle(namespace.filename)