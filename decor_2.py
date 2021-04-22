def header_footer(fn):
    def wrapper():
        print("========")
        result = fn()
        print("========")
        return result
    return wrapper


def header_footer_maker(word):
    def header_footer_2(fn):
        def wrapper(*args, **kwargs):
            print(word)
            result = fn(*args, **kwargs)
            print(word)
            return result

        return wrapper
    return header_footer_2


@header_footer_maker("++++++++")
def my_func_2():
    print("Hello World")


@header_footer
def my_func():
    print('Hello World')


if __name__ == '__main__':

    my_func()
    my_func_2()
