from typing import List

def findJudge(N: int, trust: List[List[int]]):
    trustee = set()
    judge = -1
    for t in trust:
        if t[0] not in trustee:
            trustee.add(t[0])
    for t in trust:
        if t[1] not in trustee and judge != t[1]:
            judge = t[1]

    return judge

if __name__ == "__main__":
    print(findJudge(2, [[1,2]]))
    print(findJudge(3, [[1,2],[2,3]]))
    print(findJudge(3, [[1,3],[2,3],[3,1]]))
    print(findJudge(3, [[1,3],[2,3]]))
    print(findJudge(4, [[1,3],[1,4],[2,3],[2,4],[4,3]]))
