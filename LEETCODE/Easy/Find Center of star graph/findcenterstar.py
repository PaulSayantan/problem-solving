from typing import List

def findCenter(edges: List[List[int]]) -> int:
    first = edges[0][0]
    second = edges[0][1]
    if first == edges[1][0] or first == edges[1][1]:
        return first
    else:
        return second

