result = list()
for _ in range(int(input())):
    num = int(input())
    cnt = 0
    for digit in str(num):
        digit = int(digit)
        if digit != 0 and num % digit == 0:
            cnt += 1
    
    result.append(cnt)

[print(r) for r in result]