'''
Your job is to change the string s using a non-negative integer n.

Each bit in n will specify whether or not to swap the case for each 
alphabetic character in s. When you get to the last bit of n, circle 
back to the first bit. If the bit is 1, swap the case. If its 0, don't swap the case.

You should skip the checking of bit when a non-alphabetic character is encountered, 
but they should be preserved in their original positions.
'''



'''Simplified Solution'''
from itertools import cycle

def swap(s,n):
    b = cycle(bin(n)[2:])
    return "".join(c.swapcase() if c.isalpha() and next(b) == '1' else c for c in s)



'''Descriptive Solution'''
def swap(s: str, n: int)-> str:
    string = list()
    binary = bin(n).replace('0b', '')
    pos = 0
    for i in s:
        if i.isalpha():
            if binary[pos] == '1':
                string.append(i.swapcase())
                pos += 1
            else:
                string.append(i)
                pos += 1
        else:
            string.append(i)
        if pos == len(binary):
            pos = 0
    
    return ''.join(string)



if __name__ == "__main__":
    res = swap('the lord of the rings', 0)
    print(res)