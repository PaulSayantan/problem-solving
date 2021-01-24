# from collections import Counter

# _ = input()
# arr = Counter([int(x) for x in input().split()])
# print(arr.most_common()[0][0])

input()
def migratoryBirds(arr):
    count = [0]*10
    for i in arr:
        count[i] += 1
    return count.index(max(count))

arr = map(int,input().split())
print(migratoryBirds(arr))  