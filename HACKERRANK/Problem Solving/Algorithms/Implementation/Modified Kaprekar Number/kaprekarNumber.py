from typing import List

def modified_kaprekar(start: int, end: int) -> List[int]:
    flag = False
    for num in range(start, end + 1):
        if isKaprekar(num): 
            flag = True
            print(num, end=" ")
    if not flag: print('INVALID RANGE')


def isKaprekar(num: int):
    sq_num = num * num
    l = (len(str(sq_num)) // 2) if len(str(sq_num)) % 2 == 0 else (len(str(sq_num)) // 2) + 1
    right = sq_num % (10 ** l)
    left = sq_num // (10 ** l)

    return left + right == num


if __name__ == '__main__':
    modified_kaprekar(1, 100)
    modified_kaprekar(400, 700)

        