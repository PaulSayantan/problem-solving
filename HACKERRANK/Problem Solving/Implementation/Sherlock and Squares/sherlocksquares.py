from math import ceil, sqrt

for _ in range(int(input())):
    a, b = (int(x) for x in input().split())
    i = ceil(sqrt(a))
    cnt = 0
    while i <= sqrt(b):
        i += 1
        cnt += 1
    
    print(cnt)
