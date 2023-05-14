import math

x = 10


def my_func(a):
    return math.sin(a + x)


def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("func start")
        res = func(*args, **kwargs)
        print("Func end")
        return res

    return wrapper


# @my_decorator
def for_dec(a):
    print("Hello World!", a)


X = 12


class A:
    tmp = "Daria"

    @staticmethod
    def ret_bob():
        return A.tmp

    def my_method(self, x):
        return x + 5


class B:
    @staticmethod
    @my_decorator
    def another_method(k):
        print("Hi:)")
        return math.sin(k * X)


class C(A, B):
    def __init__(self):
        self.coca = "Cola"

    def testik(self, k):
        return k