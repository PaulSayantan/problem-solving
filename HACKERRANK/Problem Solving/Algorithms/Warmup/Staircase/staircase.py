def staircase(n: int):
    space = " "
    symbol = "*"
    for i in range(1, n+1):
        print("%s%s" %(space*(n - i), symbol*i))

if __name__ == '__main__':
    n = int(input())
    staircase(n)