from typing import List
import unittest

def runningSum(nums: List[int]) -> List[int]:
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]
    return nums

class runningSumTest(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(runningSum([1,1,1,1,1]), [1,2,3,4,5])
    def test_case2(self):
        self.assertEqual(runningSum([1,2,3,4]), [1,3,6,10])
    def test_case3(self):
        self.assertEqual(runningSum([3,1,2,10,1]), [3,4,6,16,17])

if __name__ == "__main__":
    unittest.main()