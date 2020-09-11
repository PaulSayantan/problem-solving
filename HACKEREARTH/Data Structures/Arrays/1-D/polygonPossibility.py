result = list()
for _ in range(int(input())):
    _ = int(input())
    edges = [int(x) for x in input().split()]
    for i in edges:
        if 2*i >= sum(edges):
            result.append('No')
            break
    else:
        result.append('Yes')

[print(r) for r in result]