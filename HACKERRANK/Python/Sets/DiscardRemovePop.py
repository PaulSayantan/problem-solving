int(input())
nums = set([int(x) for x in input().split()])
for _ in range(int(input())):
    command = input()
    if command == 'pop':
        nums.pop()
    else:
        comm, n = (command.split())
        if comm == 'remove':
            nums.remove(int(n))
        elif comm == 'discard':
            nums.discard(int(n))
print(sum(nums))
