import sys
import os


if __name__ == '__main__':
    print(sys.argv)
    print(os.path.basename(sys.argv[0]))
    print(os.path.dirname(sys.argv[0]))

