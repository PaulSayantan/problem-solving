from itertools import groupby

numbers = [int(x) for x in input()]
for (key,group) in groupby(numbers): 
    print((len(list(group)), key), end=' ')