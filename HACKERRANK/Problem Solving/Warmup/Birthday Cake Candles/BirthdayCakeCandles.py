from collections import Counter

def birthdayCakeCandles(ar):
    count = Counter(ar)
    return count[max(ar)]

if __name__ == '__main__':
    ar_count = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = birthdayCakeCandles(ar)
    print(str(result) + '\n')
