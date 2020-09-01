nums = []
for _ in range(int(input())):
    nums.append((input().split()))
for (i, j) in nums:
    try:
        print(int(i)//int(j))
    except ZeroDivisionError as e:
        print("Error Code:", e)
    except ValueError as e:
        print("Error Code:", e)