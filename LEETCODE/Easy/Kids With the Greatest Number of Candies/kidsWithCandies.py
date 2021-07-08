"""
Problem:
		Given the array candies and the integer extraCandies, 
		where candies[i] represents the number of candies that the ith kid has.

		For each kid check if there is a way to distribute extraCandies among the kids 
		such that he or she can have the greatest number of candies among them. 

		Notice that multiple kids can have the greatest number of candies.
"""

import unittest
from typing import List

def kidsWithCandies(candies: List[int], extraCandies: int) -> List[bool]:
	highest = max(candies)
	return [(highest - candy) <= extraCandies for candy in candies]


class Test(unittest.TestCase):
	def testcase_1(self):
		self.assertEqual(kidsWithCandies([4,2,1,1,2], 1), [True, False, False, False, False])

	def testcase_2(self):
		self.assertEqual(kidsWithCandies([2,3,5,1,3], 3), [True, True, True, False, True])

	def testcase_3(self):
		self.assertEqual(kidsWithCandies([12,1,12], 10), [True, False, True])


if __name__ == '__main__':
	unittest.main()