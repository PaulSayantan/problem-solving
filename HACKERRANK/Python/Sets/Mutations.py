int(input())
nums = set([int(x) for x in input().split()])
for _ in range(int(input())):
    command, arg = (input().split())
    if command == 'update':
        nums.update([int(x) for x in input().split()])
    elif command == 'intersection_update':
        nums.intersection_update([int(x) for x in input().split()])
    elif command == 'symmetric_difference_update':
        nums.symmetric_difference_update([int(x) for x in input().split()])
    else:
        nums.difference_update([int(x) for x in input().split()])
print(sum(nums))
