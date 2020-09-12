_, charges = int(input()), str(input())
charge_stack = list()
for i in charges:
    if len(charge_stack) == 0:
        charge_stack.append(i)
    elif charge_stack[-1] == i:
        charge_stack.pop(-1)
    else:
        charge_stack.append(i)
print(''.join(charge_stack))