import json


def to_json_file(obj, filename, indent=1):
    with open(filename, "w") as f:
        json.dump(obj, f, indent=indent)


def to_json_file_oneline(obj, filename, indent=1):
    with open(filename, "w") as f:
        json.dump(obj, f, separators=(",", ":"))


if __name__ == '__main__':
    dict_json = {
        1: 1,
        "2": 5,
        "str": [122, 0x123, 123],
        "tuple": (1, 2, 3),
        "d": {1: 5},
    }
    to_json_file(dict_json, "json_indent_4", 4)
    to_json_file_oneline(dict_json, "json_oneline")