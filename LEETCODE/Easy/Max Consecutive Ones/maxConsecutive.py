#!/usr/bin/python3

# Given a binary array, find the maximum number of consecutive 1s in the array

arr = [int(x) for x in input().split()]
count = 0
i = 0
while i < len(arr):
    if arr[i] == 1:
        count += 1
        i += 1
        while i < len(arr):
            if arr[i] == 1:
                count += 1
                i += 1
            else:
                count = 0
                break
    i += 1
print(count)
