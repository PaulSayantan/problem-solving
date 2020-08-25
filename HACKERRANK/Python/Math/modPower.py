def modPower(a: int, b: int, m: int):
    print(pow(a, b))
    if b > 0:
        print(pow(a, b, m))

if __name__ == "__main__":
    modPower(int(input()), int(input()), int(input()))