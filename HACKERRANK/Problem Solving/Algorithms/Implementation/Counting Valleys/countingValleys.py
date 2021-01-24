steps = int(input())
arr = input()
curr_level, i = 0, 0
height = 0
while steps != 0:
    if arr[i] == 'D':
        curr_level -= 1
    else:
        curr_level += 1
    
    if curr_level == 0 and arr[i] == 'U':
        height += 1
    steps -= 1
    i += 1
print(height)