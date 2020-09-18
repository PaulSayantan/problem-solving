from typing import List

def BinarySearch(sorted_arr: List[int], low: int, high: int, target: int) -> int:
    while(low <= high):
        mid = (high + low) // 2
        if sorted_arr[mid] > target:
            high = mid - 1
        elif sorted_arr[mid] < target:
            low = mid + 1
        else:
            return mid
    return -1

N = int(input())
M = [int(x) for x in input().split()]
result = list()
for _ in range(int(input())):
    kill, power = 0, 0
    bishu = int(input())
    if bishu < M[N-1]:
        pos = BinarySearch(M, M[0], M[N - 1], bishu)
        if pos != -1:
            for i in range(pos + 1):
                kill += 1
                power += M[i]
            result.append((kill, power))
        else:
            i = 0
            p = M[i]
            while p < M[i+1]:
                kill += 1
                power += p
                i += 1
                p = M[i]
            result.append((kill, power))
    else:
        result.append((N, sum(M)))

[print(*r) for r in result]