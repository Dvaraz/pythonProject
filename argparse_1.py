import argparse


def createParser():
    pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("a", type=int, help="Argument one")
    parser.add_argument("b", type=int, help="Argument two")
    namespace = parser.parse_args()
    print(namespace)
    print(namespace.a + namespace.b)