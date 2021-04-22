def check_iter_object(fn):
    def wrapper(*args, **kwargs):
        for index, arg in enumerate(args, start=1):
            try:
                iter(arg)
            except TypeError:
                msg = f"Объект #{index}: {arg} не является итерируемым"
                raise TypeError(msg)

        for key, value in kwargs.items():
            try:
                iter(value)
            except TypeError:
                msg = f"Объект #{key}: {value} не является итерируемым"
                raise TypeError(msg)

        result = fn(*args, **kwargs)
        return result
    return wrapper



@check_iter_object
def slist(str_):
    print(str_)


if __name__ == '__main__':

    # slist("ada")
    # slist("ada", 12)
    slist(a = 1)