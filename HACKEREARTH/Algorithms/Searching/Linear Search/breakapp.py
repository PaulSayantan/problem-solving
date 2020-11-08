num_weight = dict()
d_date = 0
for _ in range(int(input()) // 2):
    for i in [int(x) for x in input().split() if x.isdigit()]:
        if i not in num_weight:
            num_weight[i] = 2
        else: num_weight[i] += 2
    for j in [int(x) for x in input().split() if x.isdigit()]:
        if j not in num_weight:
            num_weight[j] = 1
        else: num_weight[j] += 1

if len(num_weight) != 0:
    max_weight = max(num_weight.values())

    for key, value in num_weight.items():
        if max_weight == value:
            d_date = key

    if d_date == 19 or d_date == 20:
        print('Date')
    else: print('No Date')
else: print('No Date')