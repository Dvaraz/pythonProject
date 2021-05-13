import re


def name_secondname(string):
    a = re.compile(r"(\d)([A-Z][a-z]+)([A-Z][a-z]+)")
    a = a.findall(string)
    for position, name, second_name in a:
        yield (f"{position}) {name} {second_name}")


if __name__ == '__main__':

    table = "1NoahEmma2LiamOlivia3MasonSophia4JacobIsabella5WilliamAva6EthanMia7MichaelEmily"
    data = name_secondname(table)
    for _ in data:
        print(_)
