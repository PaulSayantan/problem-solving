import re

res = list()
for _ in range(int(input())):
    try:
        re.compile(input())
        res.append(True)
    except re.error:
        res.append(False)

[print(r) for r in res]