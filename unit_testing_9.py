import unittest  

def prime(num):
    if num>1:
        for i in range(2,num):
            if num%i == 0:
                return False
        else:
            return True
    else:
        return False
    
class CheckSum(unittest.TestCase):  
    def test_case_01(self):
        self.assertTrue(prime(29))
    def test_case_02(self):
        self.assertFalse(prime(1))
    def test_case_03(self):
        self.assertTrue(prime(11))
    def test_case_04(self):
        self.assertFalse(prime(10))

    
if __name__ == '__main__':  
    unittest.main()  
