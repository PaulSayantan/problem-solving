rev = 0
base = 1
def reverseInt(x: int) -> int:
    global rev
    global base
    neg = x < 0
    x = abs(x)
    if x not in range(-2**31 + 1, 2**31):
        return 0
    if x:
        reverseInt(int(x / 10))
        rev += (x % 10) * base
        base *= 10
    
    return rev if not neg else -rev

if __name__ == "__main__":
    print(reverseInt(int(input())))
    