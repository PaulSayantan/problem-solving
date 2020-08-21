from collections import deque

def cyclicShift(A: deque, shift: int) -> int:
    count = 0
    B = deque(A)
    B.rotate(shift-1)
    while A != B:
        B.rotate(1)
        count += 1
    B.rotate(1)
    while A != B:
        B.rotate(1)
        count += 1
    
    return count+1

res = list()
for _ in range(int(input())):
    len_bin, sh = (int(x) for x in input().split())
    res.append(cyclicShift(deque(input()), sh))
[print(result) for result in res]