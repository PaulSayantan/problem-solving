n = int(input())
res = [n]
arr = [int(x) for x in input().split()]
while len(arr) > 1:
    arr = list(filter(lambda x: x - min(arr), arr))
    if len(arr) != 0:
        res.append(len(arr))

[print(r) for r in res]