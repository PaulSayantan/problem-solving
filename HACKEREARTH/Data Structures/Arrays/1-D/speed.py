
'''Better Solution'''
result = list()
for _ in range(int(input())):
    n = int(input())
    speeds = [int(x) for x in input().split()]
    if n == 1:
        result.append(1)
        continue
    prev_speed, count = speeds[0], 1
    for curr_speed in speeds:
        if curr_speed < prev_speed:
            count += 1
            prev_speed = curr_speed
        else:
            prev_speed = curr_speed
    result.append(count)

[print(r) for r in result]


'''Best Solution'''
result = list()
for _ in range(int(input())):
    n = int(input())
    speed = list(map(int, input().split()))
    count = 0
    while len(speed) > 0:
        if speed[0] != -1:
            t = speed.pop(0)
            count += 1
        else:
            speed.pop(0)
            continue
        for i in range(len(speed)):
            if speed[i] > t:
                speed[i] = -1
    result.append(count)

[print(r) for r in result]
