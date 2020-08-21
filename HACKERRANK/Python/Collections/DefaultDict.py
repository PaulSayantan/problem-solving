from collections import defaultdict

'''Simplified Solution'''
n, m = (int(x) for x in input().split())
dd = defaultdict(list)
for i in range(n):
    dd[input()].append(str(i+1))
for _ in range(m):
    print(' '.join(dd[input()]) or -1)


'''Descriptive Solution'''
# n, m = (int(x) for x in input().split())
# A = list()
# word_dict = defaultdict(list)
# for i in range(n):
#     word_dict[str(input())].append(str(i+1))
# for _ in range(m):
#     word = input()
#     A.append(word_dict[word] or [-1])
# for i in A:
#     print(*i)