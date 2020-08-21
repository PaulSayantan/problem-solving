from collections import deque

'''Simplified Solution'''
deq = deque()
for _ in range(int(input())):
    op = input().split()
    if op[0] == 'append':
        deq.append(op[1])
    elif op[0] == 'appendleft':
        deq.appendleft(op[1])
    elif op[0] == 'pop':
        deq.pop()
    elif op[0] == 'popleft':
        deq.popleft()
print(*deq)


'''Descriptive Solution'''
# append_ops = ['append', 'appendleft']
# pop_ops = ['pop', 'popleft']
# ops_num = int(input())
# deq = deque()
# for _ in range(ops_num):
#     op = input()
#     if op in pop_ops:
#         if op.lower() == pop_ops[0]:
#             deq.pop()
#         elif op.lower() == pop_ops[1]:
#             deq.popleft()
#     else:
#         operator, value = op.split()
#         if operator.lower() == append_ops[0]:
#             deq.append(int(value))
#         elif operator.lower() == append_ops[1]:
#             deq.appendleft(int(value))

# print(*deq, sep=' ')