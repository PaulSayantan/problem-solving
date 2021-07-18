"""
Problem:
        Given two strings s and t, determine if they are isomorphic

        Two strings are isomorphic to each other only when, all characters of s can be replaced with another character,
        while preserving the order of the characters to obtain the other string
"""

def isomorphicStrings(s: str, t: str) -> bool:
    s_map = {}
    t_map = {}

    for i in range(len(s)):
        if s[i] in s_map:
            s_map[s[i]].append(i)
        else:
            s_map[s[i]] = [i]

    for j in range(len(t)):
        if t[j] in t_map:
            t_map[t[j]].append(j)
        else:
            t_map[t[j]] = [j]

    return list(s_map.values()) == list(t_map.values())

print(isomorphicStrings("egg", "add"))
print(isomorphicStrings("foo", "bar"))
print(isomorphicStrings("paper", "title"))
