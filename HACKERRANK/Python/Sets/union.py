int(input())
nums = set([int(x) for x in input().split()])
int(input())
print(len(nums.union(set([int(x) for x in input().split()]))))