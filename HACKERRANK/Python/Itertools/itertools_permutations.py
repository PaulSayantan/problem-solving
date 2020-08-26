from itertools import permutations

i= input().split(' ')
for i in sorted(list(permutations(i[0], int(i[1])))):
    s = ''
    for j in i:
        s += j
    print(s)

