import unittest
import calc

class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calc.add(10,15), 25)
        self.assertEqual(calc.add(-1,1), 0)
        self.assertEqual(calc.add(-1,-1), -2)
        
    def test_subtract(self):
        self.assertEqual(calc.subtract(10,15), -5)
        self.assertEqual(calc.subtract(-1,1), -2)
        self.assertEqual(calc.subtract(-1,-1), 0)
        
    def test_multiply(self):
        self.assertEqual(calc.multiply(10, 15), 150)
        self.assertEqual(calc.multiply(-1, 1), -1)
        self.assertEqual(calc.multiply(-1, -1), 1)
        
    def test_divide(self):
        self.assertEqual(calc.divide(15.0, 10.0), 1.5)
        self.assertEqual(calc.divide(-1, 1), -1)
        self.assertEqual(calc.divide(-1, -1), 1)
        with self.assertRaises(Exception):
            calc.divide(10/0)
        
if __name__ == "__main__":
    unittest.main()
