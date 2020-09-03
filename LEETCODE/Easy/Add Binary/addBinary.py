def addBinary(a: str, b: str) -> str:
    return bin(int(a, 2) + int(b, 2)).replace('0b', '')

if __name__ == "__main__":
    print(addBinary('1010', '1011'))