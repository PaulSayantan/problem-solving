str_list = list()
for i in range(int(input())):
    nice = 0
    str_list.append(input())
    for j in str_list:
        if j < str_list[i]:
            nice += 1
    print(nice)