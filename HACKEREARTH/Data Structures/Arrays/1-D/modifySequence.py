n = int(input())
arr = [int(x) for x in input().split()]

i = 0
while i != n - 1:
    a, b = arr[i], arr[i+1]
    if a < b:
        arr[i] = 0
        arr[i+1] -= a
    elif a > b:
        arr[i+1] = 0
        arr[i] -= b
    else:
        arr[i], arr[i+1] = 0, 0
    i += 1
    
if sum(arr) > 0:
    print("NO")
else:
    print("YES")
    