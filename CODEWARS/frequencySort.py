'''
sort elements in an array by decreasing frequency of elements. 
If two elements have the same frequency, sort them by increasing value.

solve([2,3,5,3,7,9,5,3,7]) = [3,3,3,5,5,7,7,2,9]
'''
from collections import Counter
import unittest

def solve(arr):
    new_arr = list()
    freq_arr = Counter(sorted(arr)).most_common()
    for (i, j) in freq_arr:
        new_arr += [i] * j
    return new_arr

class solveTest(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(solve([2,3,5,3,7,9,5,3,7]),[3,3,3,5,5,7,7,2,9])
    def test_case2(self):
        self.assertEqual(solve([1,2,3,0,5,0,1,6,8,8,6,9,1]),[1,1,1,0,0,6,6,8,8,2,3,5,9])
    def test_case3(self):
        self.assertEqual(solve([5,9,6,9,6,5,9,9,4,4]),[9,9,9,9,4,4,5,5,6,6])
    def test_case2(self):
        self.assertEqual(solve([4,4,2,5,1,1,3,3,2,8]),[1,1,2,2,3,3,4,4,5,8])
    def test_case4(self):
        self.assertEqual(solve([4,9,5,0,7,3,8,4,9,0]),[0,0,4,4,9,9,3,5,7,8])
    

if __name__ == "__main__":
    unittest.main()