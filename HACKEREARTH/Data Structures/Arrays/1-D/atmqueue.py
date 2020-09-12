_, queue = int(input()), [int(x) for x in input().split()]
count = 1
for i in range(len(queue) - 1):
    if queue[i] > queue[i+1]:
        count += 1
    
print(count)       