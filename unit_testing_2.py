import unittest
class TestCaseDemo(unittest.TestCase):
    def setUp(self):
        print("Setup Method")
    def test1(self):
        print("Test Method 1")
    def test2(self):
        print("Test Method 2")
    def tearDown(self):
        print("TearDown Method")
unittest.main()
