"""
Problem:
		Given two string s and t, determine if they are anagram of each other
"""

def isAnagram(s: str, t: str) -> bool:
	if s == t: return True
	if len(s) != len(t): return False

	ch_map = [0] * 128

	for ch in s:
		ch_map[ord(ch)] += 1

	for ch in t:
		if ch_map[ord(ch)] != t.count(ch):
			return False

	return True

print(isAnagram(s = "anagram", t = "nagaram"))
print(isAnagram(s = "rat", t = "car"))