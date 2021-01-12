from typing import List

def dynamic_array(n: int, queries: List[List[int]]) -> List[int]:
    lastAnswer: int = 0
    seqList = [[] for i in range(n)]
    result = []
    
    for query in queries:
        if query[0] == 1:
            x = query[1]
            y = query[2]

            seq = (x ^ lastAnswer) % n
            seqList[seq].append(y)            
        
        if query[0] == 2:
            x = query[1]
            y = query[2]

            seq = (x ^ lastAnswer) % n
            size = len(seqList[seq])
            lastAnswer = seqList[seq][y % size]
            result.append(lastAnswer)
        
        
    return result

if __name__ == "__main__":
    n, q = (int(x) for x in input().split(' '))
    queries = list()
    
    for _ in range(q):
        queries.append(list(int(x) for x in input().split(' ')))

    result = dynamic_array(n, queries)

    [print(r) for r in result]