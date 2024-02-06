import functools


def is_hex(string):
    try:
        int(string, 16)
        return True
    except ValueError:
        return False


def check(lam_func):
    def param_check(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if lam_func(args[0]) is True:
                return func(*args, **kwargs)
            else:
                print("param_check failed")
        return wrapper
    return param_check


# @check(lambda x: len(x) % 2 == 0)
@check(is_hex)
def hex_to_array(hex_string: str) -> str:
    hex_list = ["0x"+hex_string[i:i+2] for i in range(0, len(hex_string), 2)]
    arr_string = "{"+",".join(hex_list)+"}"
    return arr_string


if __name__ == "__main__":
    print(hex_to_array("123456"))
    pass
