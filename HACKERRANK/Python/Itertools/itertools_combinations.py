#   itertools.combinations(iterable, r)
#   This tool returns the  length subsequences of elements from the input iterable.

#   Combinations are emitted in lexicographic sorted order. 
#   So, if the input iterable is sorted, the combination tuples will be produced in sorted order.

from itertools import combinations

i= input().split(' ')
for j in range(1, int(i[1]) + 1):
    for k in list(combinations(sorted(i[0].upper()), j)):
        s = ''
        for a in k:
            s += a
        print(s)