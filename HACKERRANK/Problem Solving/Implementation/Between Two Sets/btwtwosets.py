from math import gcd
from typing import List
import time

def program1():
    def lcm(arr: List[int]) -> int:
        if len(arr) == 1:
            return arr[0]
        else:
            lcm = arr[0]
            for i in arr[1:]:
                lcm = int(lcm * i / gcd(lcm, i))
        
            return lcm

    def hcf(arr: List[int]) -> int:
        if len(arr) == 1:
            return arr[0]
        elif len(arr) == 2:
            return gcd(arr[0], arr[1])
        else:
            hcf = gcd(arr[0], arr[1])    
            for i in range(2, len(arr)):
                hcf = gcd(hcf, arr[i])
            
            return hcf


    n, m = (int(x) for x in input().split())
    arr_A = sorted([int(x) for x in input().split()])
    arr_B = sorted([int(x) for x in input().split()])
    start = time.perf_counter()
    i, j = lcm(arr_A), hcf(arr_B)
    count = 0
    for i in range(i, j+1, i):
        flag = 0
        for j in arr_B:
            if j % i != 0:
                flag = 1
                break
        if not flag:
            count += 1

    print(count)
    end = time.perf_counter()
    print("Time taken: ", end - start)


def program2():
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    start = time.perf_counter()
    ans = 0
    for i in range(1,101):
        flag = True
        for j in a:
            if i%j!=0:
                flag = False
                break
        if flag:
            for k in b:
                if k%i!=0:
                    flag = False
                    break
        if flag:
            ans+=1
    print(ans)
    end = time.perf_counter()
    print("Time taken: ", end - start)


if __name__ == "__main__":
    program1()
    program2()
