from collections import Counter
res = list()
for _ in range(int(input())):
    _ = input()
    h_arr = Counter(sorted([int(x) for x in input().split()]))
    maxi = max(h_arr.values())
    mini = min(h_arr.values())
    if (maxi - mini) > 0:
        res.append(maxi - mini)
    else:
        res.append(-1)

[print(r) for r in res]