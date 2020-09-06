inp, k = input().split()
comb = list()
for i in range(len(inp)):
    comb.append([inp[i:]])
print(*sorted(comb)[int(k) - 1])