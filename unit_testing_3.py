import unittest
def fun(x):
    return x + 1

class MyTest(unittest.TestCase):
 def test(self):
     self.assertEqual(fun(6), 4)

unittest.main()
