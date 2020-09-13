result = list()
for _ in range(int(input())):
    N, K = (int(x) for x in input().split())
    alice = [int(x) for x in input().split()]
    bob = [int(x) for x in input().split()]
    max_bob = max(bob)
    time = 0
    for val in alice:
        if val <= max_bob:
            time += ((max_bob + 1) - val) * K
    result.append(time)

[print(r) for r in result]