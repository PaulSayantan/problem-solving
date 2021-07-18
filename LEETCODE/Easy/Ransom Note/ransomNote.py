"""
Problem:
		Given two stings ransomNote and magazine, return true if ransomNote 
		can be constructed from magazine and false otherwise.

		Each letter in magazine can only be used once in ransomNote.

"""

from collections import Counter

def canConstruct(ransomNote: str, magazine: str) -> bool:
    if len(ransomNote) > len(magazine): return False
    
    ransom_cnt = dict(Counter(ransomNote))
    magazine_cnt = dict(Counter(magazine))

    for ch, cnt in ransom_cnt.items():
    	if ch not in magazine_cnt:
    		return False
    	else:
    		if magazine_cnt[ch] < cnt:
    			return False

    return True

print(canConstruct(ransomNote = "a", magazine = "b"))
print(canConstruct(ransomNote = "aa", magazine = "ab"))
print(canConstruct(ransomNote = "aa", magazine = "aab"))
print(canConstruct(ransomNote = "az", magazine = "ab"))
print(canConstruct(ransomNote = "aab", magazine = "baa"))
