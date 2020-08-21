from typing import List

'''Best Solution'''
def numberGame(nums: List[int], n: int) -> List[int]:
    result = list()
    F , G = [-1] * n, [-1] * n

    stack = list()
    stack.append(0)
    for i in range(1, n):
        while(stack != [] and nums[stack[-1]] < nums[i]):
            G[stack.pop()] = i
        stack.append(i)
    
    stack = list()
    stack.append(0)
    for i in range(1, n):
        while(stack != [] and nums[stack[-1]] > nums[i]):
            F[stack.pop()] = i
        stack.append(i)
    
    return [nums[F[i]] if i != -1 and F[i] != -1 else -1 for i in G]

if __name__ == "__main__":
    print(*numberGame([3, 7, 1, 7, 8, 4, 5, 2], 8))

# arr = []
# n = int(input())
# a, b, s1, s2 = dict(), dict(), [], []
# for i in range(n):
#     arr.append(int(input()))
#     x = arr[i]
#     while(s1!=[] and s1[-1][0]<x):
#         a[s1.pop()[1]] = i
#     s1.append((x, i))
#     while(s2!=[] and s2[-1][0]>x):
#         b[s2.pop()[1]] = i
#     s2.append((x, i))
# for i in range(n):
#     if i in a:
#         if a[i] in b:
#             print(arr[b[a[i]]], end = " ")
#         else:
#             print(-1, end = " ")
#     else:
#         print(-1, end = " ")
# print()