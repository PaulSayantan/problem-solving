from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    index = dict()
    for i , n in enumerate(nums):
        if target - n in index:
            return [index[target - n], i]
        index[n] = i
    return []

if __name__ == "__main__":
    nums = [int(x) for x in input().split()]
    target = int(input())
    print(twoSum(nums, target))