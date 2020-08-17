from typing import List
from itertools import combinations

def threeSum(nums: List[int]) -> List[List[int]]:
    result = list()
    for i in combinations(sorted(nums), 3):
        if i not in result and sum(i) == 0:
            result += [i]
    return result


# Time Complexity: O(n^3)
def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    result = list()
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] == 0:
                    if [nums[i], nums[j], nums[k]] in result:
                        break                    
                    else:
                        result.append([nums[i], nums[j], nums[k]])
                        break

    return result

# Time Complexity: O(n^2)
def threeSum(nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res

if __name__ == "__main__":
    print(threeSum([int(x) for x in input().split()]))

