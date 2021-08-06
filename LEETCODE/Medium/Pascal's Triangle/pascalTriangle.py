"""
Problem:
    Given an integer numRows, return the first numRows of Pascal's triangle.
    In Pascal's triangle, each number is the sum of the two numbers directly above it.
"""

from typing import List

def pascal_triangle(numRows: int) -> List[int]:
    """
    :param numRows: int
    :return: List[int]
    """
    triangle = []
    for line in range(1, numRows + 1):
        c = 1
        term = []
        for i in range(1, line + 1):
            term.append(c)
            c = c * (line - i) // i
        triangle.append(term)
    
    return triangle


if __name__ == '__main__':
    print(pascal_triangle(8))

