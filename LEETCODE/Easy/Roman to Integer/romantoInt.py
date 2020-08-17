def romantoInt(s: str) -> int:
    num = i = 0
    pairs = {'CM': 900, 'CD': 400, 'XC': 90, 'XL': 40, 'IX': 9, 'IV': 4}
    singles = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    while i < len(s):
        if i < len(s) - 1 and s[i:i+2] in pairs:
            num += pairs[s[i:i+2]]
            i += 2
        else:
            num += singles[s[i]]
            i += 1
    return num

if __name__ == "__main__":
    print(romantoInt("MCMXCIV"))