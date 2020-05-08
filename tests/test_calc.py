import unittest
import functions


class TestFunctions(unittest.TestCase):

    def test_add(self):
        self.assertEqual(functions.add(10, 5), 15)
        self.assertEqual(functions.add(-5, 5), 0)
        self.assertEqual(functions.add(-5, -5), -10)
    
    def test_subtract(self):
        self.assertEqual(functions.subtract(10, 5), 5)
        self.assertEqual(functions.subtract(-5, 5), -10)
        self.assertEqual(functions.subtract(-5, -5), 0)
    
    def test_multiply(self):
        self.assertEqual(functions.multiply(10, 5), 50)
        self.assertEqual(functions.multiply(-5, 5), -25)
        self.assertEqual(functions.multiply(-5, -5), 25)
    
    def test_divide(self):
        self.assertEqual(functions.divide(10, 5), 2)
        self.assertEqual(functions.divide(-5, 5), -1)
        self.assertEqual(functions.divide(-5, -5), 1)

        with self.assertRaises(ValueError):
            functions.divide(5, 0)


if __name__ == '__main__':
    unittest.main()
    