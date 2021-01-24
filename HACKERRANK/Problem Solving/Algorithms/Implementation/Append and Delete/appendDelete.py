import unittest

def appendAndDelete(s, t, diff):
    
    i, j, common = 0, 0, 0
    total_len = len(s) + len(t)

    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            common += 1
        else: break
        i += 1
        j += 1

    if total_len - 2 * common <= diff and total_len % 2 == diff % 2 or total_len < diff: return "Yes"
    else: return "No"


class Test(unittest.TestCase):
    def testcase1(self):
        self.assertEqual(appendAndDelete('hackerhappy', 'hackerrank', 9), 'Yes', "Test Case 1 Failed")
    def testcase2(self):
        self.assertEqual(appendAndDelete('abcd', 'abcdert', 10), 'No', "Test Case 2 Failed")
    def testcase3(self):
        self.assertEqual(appendAndDelete('y', 'yu', 2), 'No', "Test Case 3 Failed")
    def testcase4(self):
        self.assertEqual(appendAndDelete('zzzzz', 'zzzzzzz', 4), 'Yes', "Test Case 4 Failed")


if __name__ == "__main__":
    unittest.main()