from collections import defaultdict
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sums = defaultdict(int)
        count, curr_sum = 0, 0
        for i in nums:
            curr_sum += i
            if curr_sum == k:
                count += 1
            if curr_sum - k in sums:
                count += sums[curr_sum - k]
            sums[curr_sum] += 1
        return count