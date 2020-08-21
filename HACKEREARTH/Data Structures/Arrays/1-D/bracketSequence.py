'''Better Solution'''
def bracketSequences(s: str) -> int:
    res = 0
    for i in range(len(s)):
        bal = 0
        j = i
        while j < len(s) + i:
            if s[j % len(s)] == '(':
                bal += 1
            else:
                bal -= 1

            if bal < 0:
                break
            j += 1

        if bal == 0:
            res += 1
        
    return res

'''Best Solution'''
def bracketSequences(s: str) -> int:
    pointer = 0
    temp = 0
    res = 0
    for i in s:
        if(i=='('):
            pointer += 1
        else:
            pointer -= 1
        if (pointer < temp):
            temp = pointer
            res = 0
        if(temp==pointer):
            res += 1
    if pointer:
        return 0
    else:
        return res

if __name__ == "__main__":
    print(bracketSequences(input()))