import pickle


def to_pickle_file(obj, filename):
    if filename.endswith(".pickle"):
        with open(filename, "wb") as f:
            pickle.dump(obj, f)
    else:
        with open(filename + ".pickle", "wb") as f:
            pickle.dump(obj, f)


def read_binary():
    pass


if __name__ == '__main__':
    dict_pickle = {
        1: 1,
        "2": 5,
        (5, 7): "test",
        "str": [122, 0x123, 123],
        "tuple": (1, 2, 3),
        "d": {1: 5},
        "func": read_binary
    }
    to_pickle_file(dict_pickle, "test.pickle")