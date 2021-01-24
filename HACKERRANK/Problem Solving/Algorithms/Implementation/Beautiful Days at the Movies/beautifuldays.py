i, j, k = (int(x) for x in input().split())
day = 0
for num in range(i, j+1):
    rev_num = int(str(num)[::-1])
    if (num - rev_num) % k == 0:
        day += 1

print(day)