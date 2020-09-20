n, k, count = int(input()), int(input()), 0
arr = [int(x) for x in input().split()]
for i in range(n):
    for j in range(1, n):
        if (arr[i] + arr[j]) % k == 0 and i < j:
            count += 1

print(count)