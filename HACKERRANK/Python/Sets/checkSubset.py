for _ in range(int(input())):
    int(input())
    A = set([int(x) for x in input().split()])
    int(input())
    print(A.issubset(set([int(x) for x in input().split()])))