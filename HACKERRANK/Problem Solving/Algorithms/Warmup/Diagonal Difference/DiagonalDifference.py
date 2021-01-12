import numpy as np

def DiagonalDifference(arr):
    matrix = np.array(arr)  
    return abs(sum(matrix.diagonal()) - sum(np.fliplr(matrix).diagonal()))

# def DiagonalDifference(arr):
#     left = sum([ arr[i][i] for i in range(len(arr)) ])
#     right = sum([ arr[len(arr) -1 - i][i] for i in range(len(arr))])
#     return abs(left - right)

if __name__ == "__main__":
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = DiagonalDifference(arr)

    print(result)