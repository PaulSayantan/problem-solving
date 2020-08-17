def lengthOfLongestSubstring(s: str) -> int:
    left = length = 0
    visited = dict()

    for pos, char in enumerate(s):
        if char in visited and visited[char] >= left:
            left = visited[char] + 1
        else:
            length = max(length, pos - left + 1)
        visited[char] = pos
    
    return length


# def lengthOfLongestSubstring(s: str) -> int:
#     left = pos = length = 0
#     visited = dict()
    
#     while pos < len(s):
#         if visited.__contains__(s[pos]):
#             left = max(visited.get(s[pos]), left)
#         length = max(length, pos - left + 1)
#         visited[s[pos]] = pos + 1
#         pos += 1
    
#     return length

if __name__ == "__main__":
    print(lengthOfLongestSubstring(input()))