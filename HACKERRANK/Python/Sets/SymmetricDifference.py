from typing import Set

def symmetricDifference(M: Set[int], N: Set[int]) -> Set[int]:
    return M.symmetric_difference(N)

if __name__ == "__main__":
    m = int(input())
    M = set([int(x) for x in input().split()])
    n = int(input())
    N = set([int(x) for x in input().split()])
    [print(element) for element in sorted(symmetricDifference(M, N))]