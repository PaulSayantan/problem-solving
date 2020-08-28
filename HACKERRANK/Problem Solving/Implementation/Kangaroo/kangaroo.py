def kangaroo(x1, v1, x2, v2) -> str:
    if v1 == v2:
        return 'NO'
    if x2 > x1 and v2 > v1:
        return 'NO'
    while True:
        x1 = x1 + v1
        x2 = x2 + v2
        print(x1, x2)
        if x1 > x2:
            return 'NO'
        if x1 == x2:
            return 'YES'
        
if __name__ == '__main__':

    x1V1X2V2 = input().split()
    x1 = int(x1V1X2V2[0])
    v1 = int(x1V1X2V2[1])
    x2 = int(x1V1X2V2[2])
    v2 = int(x1V1X2V2[3])
    result = kangaroo(x1, v1, x2, v2)
    print(result)