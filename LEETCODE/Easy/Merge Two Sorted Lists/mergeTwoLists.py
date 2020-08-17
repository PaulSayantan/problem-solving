from typing import List

def mergeTwoLists(l1: List[int], l2: List[int]) -> List[int]:
    return sorted(l1 + l2)

if __name__ == "__main__":
    list1 = [int(x) for x in input().split()]
    list2 = [int(x) for x in input().split()]
    print(mergeTwoLists(list1, list2))

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# class MergeTwoLists:
#     def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
#         if not l1:
#             return l2
#         if not l2:
#             return l1
        
#         if l1.val < l2.val:
#             head = l1
#             tail = self.mergeTwoLists(l1.next, l2)
#         else:
#             head = l2
#             tail = self.mergeTwoLists(l1, l2.next)
        
#         head.next = tail
#         return head