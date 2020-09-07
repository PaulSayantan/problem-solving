import unittest

def mySqrt(x: int) -> int:
    # Newton's Method
    n = x/2
        
    while abs(n*n - x) > 0.005:
        n = (n+(x/n))/2
    return int(n)

if __name__ == '__main__':
    print(mySqrt(int(input())))