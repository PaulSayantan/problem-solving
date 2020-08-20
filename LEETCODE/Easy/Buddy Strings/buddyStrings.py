import unittest
from itertools import permutations

'''Simplified Solution'''
def buddyStrings(A: str, B: str) -> bool:
    if len(A) != len(B) or len(A) < 2:
            return False

    diffs = [[a, b] for a, b in zip(A, B) if a != b]
    if len(diffs) == 2:
        return diffs[0][::-1] == diffs[1]

    return len(diffs) == 0 and len(set(A)) < len(A)


'''Descriptive Solution'''
# def buddyStrings(A: str, B: str) -> bool:
#     if len(A) == 2:
#         if A[::-1] == B:
#             return True
#         else:
#             return False
#     if len(A) != len(B):
#         return False
    

#     for i in range(len(A)):
#         for j in range(1, len(A)):
#             if i == j:
#                 continue
#             str_dict = dict(enumerate(A))
#             temp = str_dict[i]
#             str_dict[i] = str_dict[j]
#             str_dict[j] = temp

#             if ''.join(str_dict.values()) == B:
#                 return True

#     return False

class buddyStringsTest(unittest.TestCase):
    def testCase1(self):
        self.assertEqual(buddyStrings('aa', 'aa'), True)
    def testCase2(self):
        self.assertEqual(buddyStrings('ab', 'ba'), True)
    def testCase3(self):
        self.assertEqual(buddyStrings('aa', 'ab'), False)
    def testCase4(self):
        self.assertEqual(buddyStrings('aaaaaaabc', 'aaaaaaacb'), True)
    def testCase5(self):
        self.assertEqual(buddyStrings('', 'aa'), False)
    def testCase5(self):
        self.assertEqual(buddyStrings('abcd', 'abcd'), False)
    def testCase6(self):
        self.assertEqual(buddyStrings('abab', 'abab'), True)

    if __name__ == "__main__":
        unittest.main()