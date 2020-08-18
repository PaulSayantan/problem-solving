import unittest
from typing import List

def findNumbers(nums: List[int]) -> int:
    return sum([len(str(i))%2==0 for i in nums])

class findNumbersTest(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(findNumbers([12,345,2,6,7896]), 2)
    def test_case2(self):
        self.assertEqual(findNumbers([555,901,482,1771]), 1)

if __name__ == "__main__":
    unittest.main()