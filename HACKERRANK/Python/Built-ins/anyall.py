_, nums = input(), [int(x) for x in input().split()]
print(all(num > 0 for num in nums) and any(str(num) == str(num)[::-1] for num in nums))