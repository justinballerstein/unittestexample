import unittest
import pythagorean

class TestHappyPath(unittest.TestCase):

    def setUp(self):
        self.py = pythagorean.Pythagorean()
        print("start of test")

    def test_three_four_five_triangle(self):
        print("test_three_four_five_triangle")
        # arrange
        a = 3
        b = 4
        expected_c = 5
        # act
        c = self.py.theorem(a,b)
        # assert
        self.assertEqual(c, expected_c)

    def tearDown(self):
        print("end of test")
        self.a = 0

class TestErrorConditions(unittest.TestCase):

    def test_zero_length_side(self):
        """Test Zero Length Side AC124"""
        py = pythagorean.Pythagorean()
        # arrange
        a = 3
        b = 0

        # act
        c = py.theorem(a,b)
        # assert
        self.assertIsNone(c)


def suite():
    suite = unittest.TestSuite()
    suite.addTest(TestHappyPath("test_three_four_five_triangle"))
    suite.addTest(TestErrorConditions("test_zero_length_side"))
    print(suite.countTestCases())
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())