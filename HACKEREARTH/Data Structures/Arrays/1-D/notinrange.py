n = int(input())
nums = list()
pointer = 1
for _ in range(n):
    x, y = (int(x) for x in input().split())
    if x in nums:
        nums.remove(x)
        continue
    if y in nums:
        nums.remove(y)
        continue
    while pointer < x:
        nums.append(pointer)
        pointer += 1
    else:
        pointer = y + 1
if len(nums) != 5:
    for i in range(pointer, 10**6+1):
        nums.append(i)

print(*nums)