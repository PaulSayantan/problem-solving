#   itertools.combinations_with_replacement(iterable, r)
#   This tool returns r length subsequences of elements from the input iterable 
#   allowing individual elements to be repeated more than once.

#   Combinations are emitted in lexicographic sorted order. 
#   So, if the input iterable is sorted, the combination tuples will be produced in sorted order.

from itertools import combinations_with_replacement


i= input().split(' ')
for k in list(combinations_with_replacement(sorted(i[0].upper()), int(i[1]))):
    s = ''
    for a in k:
        s += a
    print(s)