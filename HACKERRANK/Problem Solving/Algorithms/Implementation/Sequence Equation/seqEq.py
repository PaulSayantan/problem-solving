_ = int(input())

arr = {x: i+1 for i, x in enumerate([int(x) for x in input().split()])}
for i in range(len(arr)):
    print(arr[arr[i+1]])