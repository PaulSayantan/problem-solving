#!/bin/python3


n = int(input().strip())
a = [int(x) for x in input().split()]

from collections import Counter
d = Counter(a)
best = 0
for i in range(n+1):
    best = max(d[i] + d[i+1], best)
print(best)

# n = int(input())
# arr = [int(x) for x in input().split()]
# maxi = 0
# for i in arr:
#     curr = arr.count(i)
#     prev = arr.count(i-1)
#     curr = curr + prev
#     if curr > maxi:
#         maxi = curr

# print(maxi)