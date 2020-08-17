from collections import OrderedDict

'''Simplified Solution'''
items_dict = OrderedDict()
for _ in range(int(input())):
    name, price = input().rsplit(' ', 1)
    items_dict[name] = items_dict.get(name, 0) + int(price)
[print(item, items_dict[item]) for item in items_dict]

'''Descriptive Solution'''
# items_num = int(input())
# items_dict = OrderedDict()
# for _ in range(items_num):
#     name, price = (input().rsplit(' ', 1))
#     if name in items_dict.keys():
#         items_dict[name] += int(price)
#     else:
#         items_dict[name] = int(price)
# [print(item, items_dict[item]) for item in items_dict]