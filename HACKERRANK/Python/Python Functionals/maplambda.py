from typing import List

cube = lambda x: x**3

def fibonacci(n: int) -> List[int]:
    if n == 0:
        return []
    if n == 1:
        return [0]
    nums = [0, 1]
    for i in range(2, n):
        nums.append(nums[i-1] + nums[i-2])
    
    return nums


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))