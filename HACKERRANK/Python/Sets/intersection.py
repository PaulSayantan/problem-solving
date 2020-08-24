int(input())
nums = set([int(x) for x in input().split()])
int(input())
print(len(nums.intersection(set([int(x) for x in input().split()]))))