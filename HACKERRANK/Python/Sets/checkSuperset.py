nums = set([int(x) for x in input().split()])
flag = True
for _ in range(int(input())):
    if not nums.issuperset([int(x) for x in input().split()]):
        flag = False
print(flag)
