_ = int(input())
arr = reversed(sorted([int(x) for x in input().split()]))
max_sum, min_sum = 0, 0

subset_pos, subset_neg = list(), list()

for i in range(len(arr)):
    if arr[i] >= 0:
        max_sum += arr[i]
        subset_pos.append(arr[i])
    else:
        min_sum += arr[i]
        subset_neg.append(arr[i])
        break

if subset_pos > subset_neg:
    print(max_sum, len(subset_pos))
else:
    print(min_sum, len(subset_neg))

