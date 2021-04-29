import argparse


def count_1(start, step, count):
    current_num = start
    for _ in range(count):
        yield current_num
        current_num += step


def createParser():
    parser1 = argparse.ArgumentParser()
    parser1.add_argument("-start", type=int, help="Start of the progression")
    parser1.add_argument("-step", type=int, help="Step of the progression")
    parser1.add_argument("-count", type=int, default=5, help="Number of counts")

    subparser = parser1.add_subparsers(dest="command")
    save_parser = subparser.add_parser("save")
    save_parser.add_argument("-o", required=True, help="Save in file")
    show_parser = subparser.add_parser("show")
    # show_parser.add_argument("show", help="show 1")
    return parser1


if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args()

    if namespace.command == "show":
        for _ in count_1(namespace.start, namespace.step, namespace.count):
            print(_)
