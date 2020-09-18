len_A = int(input())
A = [int(x) for x in input().split()]
_ = int(input())
C = [int(x) for x in input().split()]
B = set()

for i in range(abs(max(C) - max(A)) + 1):
    count = 0
    for j in A:
        if i+j in C:
            count += 1
    
    if count == len_A:
        B.add(i)
        

print(*B)