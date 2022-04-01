#https://www.youtube.com/watch?v=6tNS--WetLI
import unittest
import calc

class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calc.add(0,0), 0)
        self.assertEqual(calc.add(10,5), 15)
        self.assertEqual(calc.add(-1,1), 0)
        self.assertEqual(calc.add(-1,-1), -2)

if __name__ == '__main__':
    unittest.main()