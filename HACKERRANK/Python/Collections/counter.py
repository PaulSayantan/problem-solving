from collections import Counter

'''Simplified Solution'''
income = 0
shoes_num, shoes_dict = int(input()), Counter([int(x) for x in input().split()])
for _ in range(int(input())):
    size, price = (int(x) for x in input().split())
    if shoes_dict[size]:
        income += price
        shoes_dict.subtract([size, ])
print("Total Income: ",income)



'''Descriptive Solution'''
# income = 0
# shoes_num = int(input())
# shoes_list = [int(x) for x in input().split()]
# shoes_dict = Counter(shoes_list)
# customers_num = int(input())
# for _ in range(customers_num):
#     size, price = (int(x) for x in input().split())
#     if shoes_dict[size] > 0:
#         income += price
#         shoes_dict.subtract([size, ])
# print("Total Income: ",income)
        