from typing import List

def plusOne(digits: List[int]) -> List[int]:
    numstr = [str(i) for i in digits]
    return [int(i) for i in str(int(''.join(numstr)) + 1)]


if __name__ == "__main__":
    print(plusOne([1, 2, 3, 4, 5, 6, 7, 8, 9]))