import unittest
from typing import List

def searchInsert(nums: List[int], target: int) -> int:
    if target in nums:
        return nums.index(target)
    else:
        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        for i in range(len(nums)-1):
            if nums[i] < target and target < nums[i+1]:
                return (i+1)


class searchInsertTest(unittest.TestCase):
    def testcase1(self):
        self.assertEqual(searchInsert([1, 3, 5, 6], 5), 2)
    def testcase2(self):
        self.assertEqual(searchInsert([1, 3, 5, 6], 2), 1)
    def testcase3(self):
        self.assertEqual(searchInsert([1, 3, 5, 6], 7), 4)
    def testcase4(self):
        self.assertEqual(searchInsert([1, 3, 5, 6], 0), 0)

if __name__ == "__main__":
    unittest.main()