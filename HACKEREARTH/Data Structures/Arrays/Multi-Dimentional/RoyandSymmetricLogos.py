output = []
 
def xcheck(a: list, n: int) -> bool:
    axis, r = n // 2, n // 2 * 2 if n % 2 != 0 else n // 2 * 2 - 1
    for i in range(axis):
        for j in range(n):
            if a[i][j] != a[r - i][j]:
                return False
    return True
 
 
def ycheck(a: list, n: int) -> bool:
    axis, c = n // 2, n // 2 * 2 if n % 2 != 0 else n // 2 * 2 - 1
    for i in range(n):
        for j in range(axis):
            if a[i][j] != a[i][c - j]:
                return False
    return True
 
for _ in range(int(input())):
        n, arr = int(input()), list()
        for i in range(n):
                arr.append(list(map(int, input())))
        output.append(xcheck(arr, n) and ycheck(arr, n))
 
for o in output:
    if o:
        print("YES")
    else:
        print("NO")