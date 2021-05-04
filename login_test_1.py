import argparse

"""For login
1. take argument (login)
2 if login exist:
    if login is right, take password
    if password is right grant access
3 if login does not exist:
    ask: do you want to create a new account
3.1 if yes:
  take login and password of new account
  chek if the account name is unique
  is unique:
      create new account
  is_not unique:
      ask for a new login
3.2 if no:
  finish the program
  """


def create_sub_parser(parser1):
    subparser = parser1.add_subparsers(dest="command")
    login_parser = subparser.add_parser("log_in")
    sing_ing_parser = subparser.add_parser("sing_in")


def create_parser():
    parser = argparse.ArgumentParser()
    # group = parser.add_mutually_exclusive_group()
    # group.add_argument("-log_in", action="store_true")
    # group.add_argument("-sing_in", action="store_true")
    # parser.add_argument("-login", required=True, help="Write your login")
    create_sub_parser(parser)
    return parser


if __name__ == '__main__':
    parser = create_parser()
    namespace = parser.parse_args()

