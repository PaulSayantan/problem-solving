'''Simplified Solution'''
def countApplesAndOranges(s, t, a, b, apples, oranges):
    apple_count = sum([1 for apple in apples if apple+a in range(s, t+1)])
    orange_count = sum([1 for orange in oranges if orange+b in range(s, t+1)])
    print(apple_count)
    print(orange_count)

'''Descriptive Solution'''
# def countApplesAndOranges(s, t, a, b, apples, oranges):
#     apple_count = orange_count = 0
#     for apple in apples:
#         if apple+a in range(s, t+1):
#             apple_count += 1
#     for orange in oranges:
#         if orange+b in range(s, t+1):
#             orange_count += 1
#     print(apple_count)
#     print(orange_count)


if __name__ == '__main__':
    st = input().split()
    s = int(st[0])
    t = int(st[1])
    ab = input().split()
    a = int(ab[0])
    b = int(ab[1])
    mn = input().split()
    m = int(mn[0])
    n = int(mn[1])
    apples = list(map(int, input().rstrip().split()))
    oranges = list(map(int, input().rstrip().split()))
    countApplesAndOranges(s, t, a, b, apples, oranges)