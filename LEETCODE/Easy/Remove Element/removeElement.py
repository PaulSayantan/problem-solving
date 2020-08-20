import unittest
from typing import List

def removeElement(nums: List[int], val: int) -> int:
    while val in nums:
        nums.remove(val)
    return len(nums)


class removeElementTest(unittest.TestCase):
    def testcase1(self):
        self.assertEquals(removeElement([3,2,2,3], 3), 2)
    def testcase2(self):
        self.assertEquals(removeElement([0,1,2,2,3,0,4,2], 2), 5)

if __name__ == "__main__":
    unittest.main()