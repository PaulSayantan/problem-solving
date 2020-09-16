'''
Digital root is the recursive sum of all the digits in a number.

Given n, take the sum of the digits of n. 
If that value has more than one digit, continue reducing in this way until a single-digit number is produced.

This is only applicable to the natural numbers.
'''
import unittest


def digitalRoot(n:int):
    if n < 10 and n > 0:
        return n
    
    add = 0
    while n != 0:
        add += n % 10
        n = n // 10

    if add > 9:
        return digitalRoot(int(add))
    else:
        return int(add)


class digitRootTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(digitalRoot(16), 7)
    def test2(self):
        self.assertEqual(digitalRoot(942), 6)
    def test3(self):
        self.assertEqual(digitalRoot(132189), 6)
    def test4(self):
        self.assertEqual(digitalRoot(493193), 2)

if __name__ == "__main__":
    unittest.main()

