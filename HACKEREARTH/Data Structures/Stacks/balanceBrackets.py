def isValid(s: str) -> bool:
    brackets = {'(': ')', '{': '}', '[': ']'}
    stack = list()
    for brack in s:
        if brack in brackets.keys():
            stack.append(brack)
        else:
            if not stack or brackets[stack.pop()] != brack:
                return False
    
    return not stack


for _ in range(int(input())):
    brackets_str = input()
    if isValid(brackets_str):
        print('YES')
    else:
        print('NO')