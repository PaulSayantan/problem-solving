n = int(input())
arr = [int(x) for x in input().split()]
arr_pos = {i:x for i,x in enumerate(arr)}
print(*(sorted(arr_pos, key= lambda x: arr_pos[x])))
