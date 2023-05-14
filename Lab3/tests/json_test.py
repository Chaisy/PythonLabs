import unittest
import math
from DariasSerializer153501.serializer_json import serialiser_JSON
from data_test import my_func, my_decorator, for_dec, A, B,C


# @my_decorator

class JsonTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.js = serialiser_JSON()

    def test_int(self):
        ser_obj = self.js.dumps(112)
        des_obj = self.js.loads(ser_obj)

        self.assertEqual(des_obj, 112)

    def test_list(self):
        ser_obj = self.js.dumps(["cat", "dog", [1, 2, "fish"], "love"])
        des_obj = self.js.loads(ser_obj)

        self.assertEqual(des_obj, ["cat", "dog", [1, 2, "fish"], "love"])

    def test_func(self):
        ser_obj = self.js.dumps(my_func)
        des_obj = self.js.loads(ser_obj)

        self.assertEqual(des_obj(50), my_func(50))

    def test_decorator(self):
        answ = my_decorator(for_dec)
        ser_obj = self.js.dumps(my_decorator)
        des_obj = self.js.loads(ser_obj)
        dec = des_obj(for_dec)

        self.assertEqual(answ(3), dec(3))

    def test_lambda(self):
        l = lambda b: b + 25
        ser_obj = self.js.dumps(l)
        des_ob = self.js.loads(ser_obj)

        self.assertEqual(l(2), des_ob(2))

    def test_static_method(self):
        ser_obj = self.js.dumps(A)
        des_obj = self.js.loads(ser_obj)

        self.assertEqual(des_obj.ret_bob(), A.ret_bob())

    def test_decorated_static_method(self):
        obj = B()
        ser_obj = self.js.dumps(obj)
        print("-----------------------\n")
        print(ser_obj)
        print("------------------------\n")
        des_obj = self.js.loads(ser_obj)

        self.assertEqual(obj.another_method(5), des_obj.another_method(5))

    def test_method(self):
        obj = C()
        ser_obj = self.js.dumps(obj)
        des_obj = self.js.loads(ser_obj)

        self.assertEqual(obj.testik(112), des_obj.testik(112))

    def test_init(self):
        obj = C()
        ser_obj = self.js.dumps(obj)
        des_obj = self.js.loads(ser_obj)

        self.assertEqual(obj.coca, des_obj.coca)


if __name__ == "__main__":
    unittest.main()