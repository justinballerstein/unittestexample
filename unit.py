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

        # act
        c = pythagorean.Pythagorean.theorem(a,b)
        # assert
        self.assertIsNone(c)

    def test_assert_sample_two(self):
        # arrange
        a = 3
        b = 4
        expected_c = 4
        # act
        c = pythagorean.Pythagorean.theorem(a,b)
        # assert
        self.assertIsNotNone(c)
        self.assertLess(c,10)
        self.assertGreater(c,1)


if __name__ == '__main__':
    unittest.main()