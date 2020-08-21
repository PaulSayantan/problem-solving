import unittest

def isValid(s: str) -> bool:
    brackets = {'(': ')', '{': '}', '[': ']'}
    stack = list()
    for brack in s:
        if brack in brackets.keys():
            stack.append(brack)
        else:
            if not stack or brackets[stack.pop()] != brack:
                return False
    
    return not stack

class isValidTest(unittest.TestCase):
    def testcase1(self):
        self.assertEqual(isValid('()'), True)
    def testcase2(self):
        self.assertEqual(isValid('()[]{}'), True)
    def testcase3(self):
        self.assertEqual(isValid('(]'), False)
    def testcase4(self):
        self.assertEqual(isValid('([)]'), False)
    def testcase5(self):
        self.assertEqual(isValid('{[]}'), True)

if __name__ == "__main__":
    unittest.main()