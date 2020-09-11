def solve (A,N):
    sum = 0
    for i in range(N):
        if A[i] >= pow(2, N) / 2:
            sum += A[i]
    return int(sum % 1000000007)

T = int(input())
for _ in range(T):
    N = int(input())
    A = [int(x) for x in input().split()]

    out_ = solve(A,N)
    print (out_)