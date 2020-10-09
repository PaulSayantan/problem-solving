alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
h = [int(i) for i in input().split()]
alpha_map = dict(zip(alpha, h))
max_height, length = 0, 0
for i in input():
    length += 1
    if max_height < alpha_map[i]:
        max_height = alpha_map[i]

print(max_height * length)


