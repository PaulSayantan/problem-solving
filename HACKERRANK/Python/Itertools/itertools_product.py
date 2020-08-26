from itertools import product
A = list(map(lambda x: int(x), input().split()))
B = list(map(lambda x: int(x), input().split()))
for i in list(product(A, B)):
    print(i, sep=' ', end=' ')


