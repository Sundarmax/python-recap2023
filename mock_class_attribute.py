import unittest
from unittest.mock import patch,MagicMock

class calculate:

    val = 11

    def process(self):
        pass

class math:
    
    num = 10
    
    def __init__(self) -> None:
        self.num = 1
        self.dic = {"name":"sundar"}

class TestCalculate(unittest.TestCase):
    
    # mock class attribute value
    @patch.object(calculate, 'val', 2)
    def test_process(self):
        self.assertEqual(calculate.val,2)
        self.assertNotEqual(calculate.val, 3)

    # Use the patch.object Decorator to Patch the Constructor
    @patch.object(math,'__new__')
    def test_math_process(self,mock_math):
        mocked_instance = MagicMock()
        mocked_instance.num = 11
        mocked_instance.dic = {"name":"raja"}
        mock_math.return_value = mocked_instance

        self.assertEqual(math().num, 11)
        self.assertEqual(math().dic, {"name":"raja"})

if __name__ == '__main__':
    unittest.main()