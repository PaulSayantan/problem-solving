result = list()

for _ in range(int(input())):
    flag = 1
    num = sorted(input())
    for i in range(len(num) - 1):
        if abs(int(num[i]) - int(num[i + 1])) != 1:
            result.append('NO')
            flag = 0
            break
    if flag == 0:
        continue
    else:
        result.append('YES')

[print(r) for r in result]