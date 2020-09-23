n = int(input())
output = list()
arr = [int(x) for x in input().split()]
A, B = 0, n - 1
while A != n and B != -1:
    if arr[A] == arr[B]:
        output.append(0)
        A += 1
        B -= 1
    elif arr[A] < arr[B]:
        output.append(2)
        A += 1
    else:
        output.append(1)
        B -= 1

print(*output)