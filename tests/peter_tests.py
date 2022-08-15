import unittest
from peter_69 import PeTeR

class PeTeRTestCase(unittest.TestCase):
  def setUp(self):
    self.peter = PeTeR()

  def test_zero(self):
    """Test 0"""
    result = self.peter.says(0)
    self.assertEqual(result, "PeTeR says the number you gave is even.")

  def test_69(self):
    """Test odd number 69"""
    result = self.peter.says(69)
    self.assertEqual(result, "PeTeR says the number you gave is odd.\nPeTeR says nice.")   

  def test_odd_number(self):
    """Test odd number 333"""
    result = self.peter.says(333)
    self.assertEqual(result, "PeTeR says the number you gave is odd.")  

  def test_even_number(self):
    """Test even number 420"""
    result = self.peter.says(420)
    self.assertEqual(result, "PeTeR says the number you gave is even.")

  def test_negative_number(self):
    """Test negative odd number -42069"""
    result = self.peter.says(-42069)
    self.assertEqual(result, "PeTeR says the number you gave is odd.")

if __name__ == '__main__':
  unittest.main()