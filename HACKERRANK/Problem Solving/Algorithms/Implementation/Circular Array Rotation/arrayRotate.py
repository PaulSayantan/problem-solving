from collections import deque

n, k, q = (int(x) for x in input().split())
result = list()
arr = deque([int(x) for x in input().split()])
arr.rotate(k)
for _ in range(q):
    result.append(arr[int(input())])

[print(r) for r in result]