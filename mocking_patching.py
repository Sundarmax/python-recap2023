import unittest
from unittest.mock import patch,Mock

from math_1 import Calculator

class MockTest(unittest.TestCase):

    def setUp(self) -> None:
        return super().setUp()
    
    def test_mock_object(self):
        # Patch object of class
        # Use patch.object(MyClass, 'my_method', return_value="return value"):
        with patch.object(Calculator, 'add', return_value = 2):
            self.assertEqual(Calculator.add(), 2)
    
    @patch.object(Calculator, 'add', return_value = 22)
    def test_mock_method_called(self,mock_calc):
        # Mocked method is called
        mock_ins = Mock()
        mock_calc.return_value = mock_ins
        mock_calc.add()
        mock_calc.add.assert_called()

    @patch.object(Calculator, 'add', return_value = 11)
    def test_method_called_with_argument(self, mock_calc):
        # Mocked method is called with arguments
        mock_ins = Mock()
        mock_calc.return_value = mock_ins
        mock_calc.add(1,2)
        mock_calc.add.assert_called_with(1,2)


    

if __name__ == '__main__':
    unittest.main()
