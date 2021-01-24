_, k = (int(x) for x in input().split())
num_doses = max([int(x) for x in input().split()]) - k
print(num_doses if num_doses > 0 else 0)