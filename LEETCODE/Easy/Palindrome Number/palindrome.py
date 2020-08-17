def palindrome(x: int) -> bool:
    temp = x
    rev = 0
    if x % 10 == x:
        return True
    if x < 0:
        return False
    while x > 0:
        rev = rev * 10 + x % 10
        x //= 10

    return rev == temp

if __name__ == "__main__":
    print(palindrome(323))