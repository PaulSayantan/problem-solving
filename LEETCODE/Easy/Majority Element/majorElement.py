"""
Problem:

"""

def majorityElement(nums: List[int]) -> int:
    ele_hash = {}
    for ele in nums:
        if ele in ele_hash:
            ele_hash[ele] += 1
            if ele_hash[ele] > len(nums) // 2:
                return ele
        else:
            ele_hash[ele] = 1
            if 1 > len(nums) // 2:
                return ele