from typing import List

def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
        nums1 += nums2
        nums1.sort()
        if len(nums1) % 2 == 0:
            return (nums1[len(nums1) // 2 - 1] + nums1[len(nums1) // 2])/ 2 
        return nums1[len(nums1) // 2]


if __name__ == "__main__":
    l1 = [int(x) for x in input().split()]
    l2 = [int(x) for x in input().split()]
    print(findMedianSortedArrays(l1, l2))