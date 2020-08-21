from collections import Counter
from typing import List

def removeDuplicates( nums: List[int]) -> int:
    return len(Counter(nums).keys())

if __name__ == "__main__":
    print(removeDuplicates([int(x) for x in input().split()]))

# def removeDuplicates(self, nums: List[int]) -> int:
#         next = 0
#         for i in range(len(nums)):
#             if i == 0 or nums[i] != nums[i - 1]:
#                 nums[next] = nums[i]
#                 next += 1
#         return next