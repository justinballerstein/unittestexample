import unittest
import pythagorean

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        a = 3
        b = 4
        expected_c = 5
        c = pythagorean.Pythagorean.theorem(a,b)
        self.assertEqual(c, expected_c)

if __name__ == '__main__':
    unittest.main()