from typing import List

def SimilarElementsPairs(A: List[int],N: int) -> int:
    A.sort()
    count = same = ans = 0
    for i in range(1, N):
        # print("At loop", i, ":")
        # print("A[i-1]: ", A[i-1])
        # print("A[i]: ", A[i])
        if abs(A[i] - A[i-1]) == 1:
            count += 1
            # print("count: ", count, "same: ", same, "ans", ans)
        elif A[i] == A[i-1]:
            same += 1
            # print("count: ", count, "same: ", same, "ans", ans)
        else:
            if count != 0:
                count += same
                ans += (count * (count + 1)) / 2
            count = same = 0
            # print("count: ", count, "same: ", same, "ans", ans)
    if count != 0:
        count += same
        ans += (count * (count + 1)) / 2
        # print("count: ", count, "same: ", same, "ans", ans)
        
    return int(ans)

N = int(input())
A = [int(x) for x in input().split()]
out_ = SimilarElementsPairs(A,N)
print (out_)