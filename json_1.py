import json


def to_json_string(obj):
    json_string = json.dumps(obj, indent=4)
    return json_string


if __name__ == '__main__':
    dict_json = {
        1: 1,
        "2": 5,
        "str": [122, 0x123, 123],
        "tuple": (1, 2, 3),
        "d": {1: 5},
    }
    print(to_json_string(dict_json))