from typing import List

def linearSearch(arr: List[int], target: int) -> int:
    
    # if only one element in the arr -> return the arr
    if len(arr) == 1:
        return arr[0]

    # check if target is found or not
    found = False
    
    # loop through the whole array
    for i in range(len(arr)):
        # when target is found
        if arr[i] == target:
            # return position of the target
            return i
            # declare that target is found
            found = True
            # break out of the loop to ignore unecessary traversing 
            break
    
    # when target is not found -> return None 
    if not found:
        return None

_ = int(input())
print(linearSearch([int(x) for x in input().split()], int(input())))