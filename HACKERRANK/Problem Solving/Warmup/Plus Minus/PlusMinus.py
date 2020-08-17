#!/bin/python3

def plusMinus(arr):
    print("{:.6f}".format(len([x for x in arr if x > 0]) / len(arr)))
    print("{:.6f}".format(len([x for x in arr if x < 0]) / len(arr)))
    print("{:.6f}".format(len([x for x in arr if x == 0]) / len(arr)))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)