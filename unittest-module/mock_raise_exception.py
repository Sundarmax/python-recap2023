import unittest
from unittest.mock import patch,MagicMock

class A:
    def __init__(self) -> None:
        pass

    def computeData(self):
        return 0

class B:

    def method_to_test():
        obj = A()
        try:
            print(obj.computeData())
        except Exception as e:
            print("Exception at method_to_test: " + str(e))


class TestClass(unittest.TestCase):
    
    def setUp(self) -> None:
        pass

    @patch.object(A, 'computeData',MagicMock(side_effect=[1,Exception('Test'),2]))
    def test_exception(self):
        B.method_to_test()
        self.assertRaises(Exception,B.method_to_test())
        B.method_to_test()


if __name__ == '__main__':
    unittest.main()
