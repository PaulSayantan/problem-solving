from collections import deque
from typing import List


def addTwoNumbers(l1: List[int], l2: List[int]) -> List[int]:
    a = deque()
    b = deque()
    c = list()
    carry = 0
    [a.append(x) for x in l1]
    [b.append(x) for x in l2]
    while a or b or carry:
        if a:
            carry += a.pop()
        if b:
            carry += b.pop()
        c.append(carry % 10)
        carry //= 10
    return c

if __name__ == "__main__":
    list1 = [int(x) for x in input().split()]
    list2 = [int(x) for x in input().split()]
    print(addTwoNumbers(list1, list2))





# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
#     prev = result = ListNode(None)
#     carry = 0

#     while l1 or l2 or carry:
#         if l1:
#             carry += l1.val
#             l1 = l1.next
#         if l2:
#             carry += l2.val
#             l2 = l2.next
#         prev.next = ListNode(carry % 10)
#         prev = prev.next
#         carry //= 10
    
#     return result.next

    
