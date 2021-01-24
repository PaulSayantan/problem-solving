import sys
length, count = int(input()), 0

choco_arr = [int(x) for x in input().split()]
day, month = (int(x) for x in input().split())
if length == 1:
    print(1)
    sys.exit(0)
i = 0
while month <= length:
    if sum(choco_arr[i:month]) == day:
        count += 1
    i += 1
    month += 1

print(count)