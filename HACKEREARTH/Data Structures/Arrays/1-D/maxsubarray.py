n, k = (int(x) for x in input().split())
arr = [int(x) for x in input().split()]
new_arr = list()
i = 0
while i != n - k + 1:
    new_arr.append(max(arr[i:i+k]))
    i += 1

print(*new_arr)