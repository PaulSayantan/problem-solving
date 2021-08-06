def longestPalindromicSubstring(s: str) -> str:
    """
    Given a string s, return the longest palindromic substring in s.
    """
    if len(s)<1 or s==s[::-1]:
        return s
        
    start,maxlen=0,1
    for i in range(1, len(s)):
        # take substrings of odd length
        odd = s[i-maxlen-1: i+1]
        # take substrings of even length
        even = s[i-maxlen: i+1]
        # check if substring is palindrome
        if i-maxlen-1>=0 and odd==odd[::-1]:
            start=i-maxlen-1
            maxlen+=2
            #continue
        if i-maxlen>=0 and even==even[::-1]:
            start=i-maxlen
            maxlen+=1
    return s[start:start+maxlen]

print(longestPalindromicSubstring("babad"))
print(longestPalindromicSubstring("cbbd"))
print(longestPalindromicSubstring("a"))
print(longestPalindromicSubstring("ac"))