import unittest
class TestCaseDemo(unittest.TestCase):
    def setUp(self):
        print("Setup Method")
    def test(self):
        print("Test Method")
    def tearDown(self):
        print("TearDown Method")
unittest.main()
