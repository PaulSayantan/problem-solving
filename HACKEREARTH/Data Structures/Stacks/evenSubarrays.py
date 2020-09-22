for _ in range(int(input())):
    binary, stack = [i for i in input()], list()
    for i in binary:
        if len(stack) > 0 and i == stack[0]:
            stack.pop(0)
        else:
            stack.insert(0, i)
    stack.reverse()
    if len(stack) == 0:
        print('KHALI')
    else:
        print(''.join(stack))