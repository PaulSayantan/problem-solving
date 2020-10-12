#!/usr/bin/python3

shares, likes = 5, 2
for _ in range(int(input())-1):
    shares = (shares // 2) * 3
    likes += shares // 2
print(likes)

