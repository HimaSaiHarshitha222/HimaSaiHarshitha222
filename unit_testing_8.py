import unittest  
from my_sum import sum  

def sod(num):
    sum = 0
    while num>0:
        rem = num% 10
        sum = sum + rem
        num = num // 10
    return sum
class CheckSum(unittest.TestCase):  
    def test_case_01(self):  
        self.assertEqual(sod(234), 9)
    def test_case_02(self):  
        self.assertEqual(sod(876765765), 57)
    def test_case_03(self):  
        self.assertEqual(sod(0), 0)
if __name__ == '__main__':  
    unittest.main()  
