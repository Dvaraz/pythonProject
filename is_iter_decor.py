def is_iter_dec(fn):
    def wrapper(*args, **kwargs):
        try:
            for key, values in kwargs.items():
                iter(values)
        except TypeError:
            print(f"{kwargs} is not iterator")

        result = fn(args, kwargs)
        return result
    return wrapper


@is_iter_dec
def test(x, y):
    return x, y

print(test(k="123"))


