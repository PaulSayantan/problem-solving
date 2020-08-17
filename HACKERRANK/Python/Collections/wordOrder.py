from collections import Counter

'''Simplified Solution'''
word_counter = Counter([input() for _ in range(int(input()))])
print(len(word_counter))
print(*word_counter.values())


'''Descriptive Solution'''
# words_num = int(input())
# word_list = list()
# for _ in range(words_num):
#     word_list.append(input())
# word_counter = Counter(word_list)

# print(len(word_counter))
# print(*word_counter.values())

