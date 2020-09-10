from typing import List

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> List[int]:
    i, j, k = m - 1, n - 1, m + n - 1
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1
    if i < 0:
        nums1[:k+1] = nums2[:j+1]


if __name__ == "__main__":
    print(merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))