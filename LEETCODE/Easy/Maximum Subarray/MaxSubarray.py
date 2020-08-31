from typing import List
import unittest

def maxSubArray(nums: List[int]) -> int:
    max_overall = float('-inf')
    max_end = 0
    for num in nums:
        if max_end > 0:
            max_end += num
        else:
            max_end = num
        
        max_overall = max(max_overall, max_end)
    
    return max_overall

class maxSubArrayTest(unittest.TestCase):
    def testcase1(self):
        self.assertEqual(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]), 6)

if __name__ == "__main__":
    unittest.main()