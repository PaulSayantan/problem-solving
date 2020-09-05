'''Simplified Solution'''
print(*sorted(input(), key=lambda k: (k.isdigit() - k.islower(), k in '02468', k)), sep='')
        
'''Descriptive Solution'''
lower,upper,odd,even=list(), list(), list(), list()
for i in sorted(input()):
    if i.isalpha():
        x = upper if i.isupper() else lower
    else:
        x = odd if int(i)%2 else even
    x.append(i)
print("".join(lower+upper+odd+even))