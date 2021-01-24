from collections import Counter

input()
arr = Counter([int(x) for x in input().split()])
count = 0

for (_, j) in arr.items():
    if j >= 2:
        count += j // 2

print(count)
