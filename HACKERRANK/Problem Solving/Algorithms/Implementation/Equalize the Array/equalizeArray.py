from typing import List

def equalizeArray(arr: List[int]) -> int:
    counter = dict()

    for n in arr:
        if n in counter.keys():
            counter[n] += 1
        else: counter[n] = 1

    if max(counter.values()) == 1:
        return len(arr) - 1

    return len(arr) - max(counter.values())

if __name__ == '__main__':
    print(equalizeArray([3, 3, 2, 1, 3]))
    print(equalizeArray([37, 32, 97, 35, 76, 62]))
    print(equalizeArray([1, 2, 3, 1, 2, 3, 3, 3]))