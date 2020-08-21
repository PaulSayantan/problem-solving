from typing import List
import unittest

def longestcommonprefix(strs: List[str]) -> str:
    if strs == None or len(strs) == 0:
        return ''
    elif len(strs) == 1:
        return strs[0]
    i = 0
    strs.sort()
    while i < len(strs[0]) and i < len(strs[-1]) and strs[0][i] == strs[-1][i]:
        i += 1
    return strs[0][:i]


class longestcommonprefixTest(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(longestcommonprefix(['flow', 'flight', 'flower']), 'fl')
    def test_case2(self):
        self.assertEqual(longestcommonprefix(['dog', 'racecar', 'car']), '')
    def test_case3(self):
        self.assertEqual(longestcommonprefix(['ababa', 'abc', 'aba']), 'ab')


if __name__ == "__main__":
    unittest.main()