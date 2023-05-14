import unittest
import math
from DariasSerializer153501.serializer_json import serialiser_JSON

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
    bob = "sinii"

    @staticmethod
    def ret_bob():
        return A.bob

    def my_method(self, x):
        return x + 5


class B:
    @staticmethod
    @my_decorator
    def another_method(k):
        print("Hi:)")
        return math.sin(k * X)


class C(A, B):
    # def __init__(self):
    #     self.coca = "Cola"

    def abobus(self, k):
        return k


# @my_decorator

class JsonTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.js = serialiser_JSON()

    # def test_int(self):
    #     ser_obj = self.js.dumps(12)
    #     des_obj = self.js.loads(ser_obj)
    #
    #     self.assertEqual(des_obj, 12)
    #
    # def test_list(self):
    #     ser_obj = self.js.dumps([1, 2, [3, 5, "blue"], "pup"])
    #     des_obj = self.js.loads(ser_obj)
    #
    #     self.assertEqual(des_obj, [1, 2, [3, 5, "blue"], "pup"])
    #
    # def test_func(self):
    #     ser_obj = self.js.dumps(my_func)
    #     des_obj = self.js.loads(ser_obj)
    #
    #     self.assertEqual(des_obj(5), my_func(5))
    #
    # def test_decorator(self):
    #     answ = my_decorator(for_dec)
    #     ser_obj = self.js.dumps(my_decorator)
    #     des_obj = self.js.loads(ser_obj)
    #     dec = des_obj(for_dec)
    #
    #     self.assertEqual(answ(3), dec(3))
    #
    # def test_lambda(self):
    #     l = lambda b: b + 25
    #     ser_obj = self.js.dumps(l)
    #     des_ob = self.js.loads(ser_obj)
    #
    #     self.assertEqual(l(2), des_ob(2))
    #
    # def test_static_method(self):
    #     ser_obj = self.js.dumps(A)
    #     des_obj = self.js.loads(ser_obj)
    #
    #     self.assertEqual(des_obj.ret_bob(), A.ret_bob())
    #
    # def test_decorated_static_method(self):
    #     obj = B()
    #     ser_obj = self.js.dumps(obj)
    #     print("-----------------------\n")
    #     print(ser_obj)
    #     print("------------------------\n")
    #     des_obj = self.js.loads(ser_obj)
    #
    #     self.assertEqual(obj.another_method(5), des_obj.another_method(5))

    def test_method(self):
        obj = C()
        ser_obj = self.js.dumps(obj)
        des_obj = self.js.loads(ser_obj)

        self.assertEqual(obj.abobus(12), des_obj.abobus(12))

    # def test_init(self):
    #     obj = C()
    #     ser_obj = self.js.dumps(obj)
    #     des_obj = self.js.loads(ser_obj)
    #
    #     self.assertEqual(obj.coca, des_obj.coca)


if __name__ == "__main__":
    unittest.main()