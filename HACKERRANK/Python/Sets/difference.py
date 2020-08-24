int(input())
nums = set([int(x) for x in input().split()])
int(input())
print(len(nums.difference([int(x) for x in input().split()])))
