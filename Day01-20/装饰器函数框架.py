"""
装饰器函数框架 - 

Author: 蔡兆胜
Version: 1.0
2026/2/3
"""


def capitalize_every_word(func):

    def wrapper(*args, **kwargs):

        ret_value = func(*args, **kwargs)
        if type(ret_value) == str:
            ret_value = ret_value.title()
        return ret_value



    return wrapper


@capitalize_every_word
def foo():
    return 'hello world'

@capitalize_every_word
def bar():
    return 12345


print(foo())
print(bar())