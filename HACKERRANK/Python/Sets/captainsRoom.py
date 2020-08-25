from collections import Counter

n = int(input())
nums = Counter([int(x) for x in input().split()])
print(nums.most_common()[-1][0])