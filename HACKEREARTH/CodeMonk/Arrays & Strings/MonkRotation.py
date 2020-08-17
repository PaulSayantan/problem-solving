from collections import deque

for _ in range(int(input())):
    n, k = (int(x) for x in input().split())
    arr = deque([int(x) for x in input().split()])
    arr.rotate(k % n)
    print(*arr)