import unittest
import pythagorean

class TestStringMethods(unittest.TestCase):

    def test_three_four_five_triangle(self):
        # arrange
        a = 3
        b = 4
        expected_c = 5
        # act
        c = pythagorean.Pythagorean.theorem(a,b)
        # assert
        self.assertEqual(c, expected_c)

    def test_zero_length_side(self):
        # arrange
        a = 3
        b = 0
        expected_c = None
        # act
        c = pythagorean.Pythagorean.theorem(a,b)
        # assert
        self.assertEqual(c, expected_c)

if __name__ == '__main__':
    unittest.main()