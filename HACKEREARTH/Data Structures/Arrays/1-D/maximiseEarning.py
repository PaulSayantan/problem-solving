result = list()
for _ in range(int(input())):
    _, R = (int(x) for x in input().split())
    bh = [int(x) for x in input().split()]
    income, max_height = 0, 0
    for curr_height in bh:
        if curr_height > max_height:
            max_height = curr_height
            income += 1
    result.append(income * R)

[print(r) for r in result]