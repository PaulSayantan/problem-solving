import unittest

def climbStairs(n: int)-> int:
    if n <= 0: return 0
    if n <= 2: return n
    # the number of distinct ways are in fibonacci sequence
    stairs, prev = 2, 1
    for _ in range(3, n+1):
        stairs, prev = stairs + prev, stairs
    
    return stairs

class climbStairsTest(unittest.TestCase):
    def test1(self):
        self.assertEqual(climbStairs(2), 2)
    def test2(self):
        self.assertEqual(climbStairs(3), 3)
    def test3(self):
        self.assertEqual(climbStairs(4), 5)
    def test4(self):
        self.assertEqual(climbStairs(5), 8)

if __name__ == "__main__":
    unittest.main()