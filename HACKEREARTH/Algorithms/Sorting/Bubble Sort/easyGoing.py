from typing import List

def arr_sort(n: int, arr: List[int]) -> List[int]:
    for i in range(n):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    
    return arr


for _ in range(int(input())):
    n, m = (int(x) for x in input().split())
    arr = [int(x) for x in input().split()]
    arr = arr_sort(n, arr)
    print(sum(arr[m: n]) - sum(arr[: n-m]))