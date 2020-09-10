import re

n = int(input())
deciReg = re.compile(r'(^[+-]?)([0-9])*(\.[0-9]+$)')
def checkReg(s):
    mo = deciReg.search(s)
    if mo == None:
        print('False')
    else:
        print('True')

for i in range(n):
    s = input()
    checkReg(s)


# res = []
# for _ in range(int(input())):
#     try:
#         if float(input()) == 0:
#             res.append(False)
#         else:
#             res.append(True)
#     except:
#         res.append(False)

# [print(r) for r in res]