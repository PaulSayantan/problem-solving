"""
Problem:
			Given a zero-based permutation nums (0-indexed), build an array ans of the same length, 
			where ans[i] = nums[nums[i]] for each 0 <= i < nums.length and return it.

Constraint:
			Solve without using extra memory
"""
from typing import List

def buildArray(nums: List[int]) -> List[int]:
	return [nums[nums[i]] for i in range(len(nums))]

print(buildArray([0, 2, 1, 5, 3, 4]))