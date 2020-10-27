substr = input()
substr_len = len(substr)
length = int(input())
if substr == 'a':
    print(length)
else:
    full_substr = substr.count('a') * (length // substr_len)
    partial_substr = substr[: length % substr_len].count('a')
    print(full_substr + partial_substr)