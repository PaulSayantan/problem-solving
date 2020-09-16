import unittest

def is_divide_by(number, a, b):
    return (number % a) == 0 and (number % b) == 0


class is_divide_by_Test(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(is_divide_by(-12, 2, -6), True)
    def test_case2(self):
        self.assertEqual(is_divide_by(-12, 2, -5), False)
    def test_case3(self):
        self.assertEqual(is_divide_by(45, 1, 6), False)
    def test_case4(self):
        self.assertEqual(is_divide_by(45, 5, 15), True)
    def test_case5(self):
        self.assertEqual(is_divide_by(4, 1, 4), True)
    def test_case6(self):
        self.assertEqual(is_divide_by(15, -5, 3), True)
    def test_case7(self):
        self.assertEqual(is_divide_by(3459, 2, 5), False)
    def test_case8(self):
        self.assertEqual(is_divide_by(3665, 1, 1), True)
    def test_case9(self):
        self.assertEqual(is_divide_by(5944, 2, 6), False)
    def test_case10(self):
        self.assertEqual(is_divide_by(8893, 3, 3), False)

if __name__ == "__main__":
    unittest.main()

    