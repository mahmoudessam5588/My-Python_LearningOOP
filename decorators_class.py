import functools
import sys
sys.setrecursionlimit(10000)
# function decorators


def repeated_name(num_rep):
    def decorator_name(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_rep):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_name


@repeated_name(num_rep=3)
def print_name(name):
    print(f'the name is {name}')


print_name('alex')
# class decorators


class call_count:
    def __init__(self, func):
        self.func = func
        self.call_num = 0

    def __call__(self, *args, **kwargs):
        self.call_num += 1
        print(f'this is executed {self.call_num} of times')
        return self.func(*args, **kwargs)


@call_count
def say_hello():
    print('Hello')


say_hello()
say_hello()
