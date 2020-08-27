import unittest

def lengthOfLastWord(s: str) -> int:
    pos = len(s) - 1
    end = -1

    while pos >= 0:
        if s[pos] == ' ' and end != -1:
            return end - pos
        if s[pos] != ' ' and end == -1:
            end = pos
        pos -= 1

    return end + 1 if end != -1 else 0

class lengthOfLastWordTest(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(lengthOfLastWord("a"), 1)
    def test_case2(self):
        self.assertEqual(lengthOfLastWord(" a"), 1)
    def test_case3(self):
        self.assertEqual(lengthOfLastWord("Hello World"), 5)
    def test_case4(self):
        self.assertEqual(lengthOfLastWord(""), 0)

if __name__ == "__main__":
    unittest.main()