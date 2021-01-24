result = list()
for _ in range(int(input())):
    n, k = (int(x) for x in input().split())
    cnt = 0
    for i in [int(x) for x in input().split()]:
        if i <= 0:
            cnt += 1
            if cnt >= k:
                result.append('NO')
                break
    if cnt < k:
        result.append('YES')

[print(res) for res in result]