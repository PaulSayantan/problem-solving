for _ in range(int(input())):
    invert = 0
    comb = list()
    n = int(input())
    mat = [list(int(x) for x in input().split()) for _ in range(n)]
    for i in range(n):
        for j in range(n):
            comb.append((i, j))
    for i, j in comb:
        for ele in (map(lambda x: mat[x[0]][x[1]], list(filter(lambda arr: arr[0] >= i and arr[1] >= j, comb)))):
            if mat[i][j] > ele :
                invert += 1
    
    print(invert)