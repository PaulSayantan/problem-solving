def modDivmod(a: int, b: int):
    print(a // b)
    print(a % b)
    print(divmod(a, b))

if __name__ == "__main__":
    modDivmod(int(input()), int(input()))