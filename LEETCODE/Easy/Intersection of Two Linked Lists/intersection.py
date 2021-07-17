"""
Problem:
		Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. 

		If the two linked lists have no intersection at all, return null.

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Approach 1
def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    currA, currB = headA, headB
    
    while currA != currB:
        if currA == None:
            currA = headB
        else: currA = currA.next
            
        if currB == None:
            currB = headA
        else: currB = currB.next
    else:
        return currA


# Approach 2
def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
	currA, currB = headA, headB
	node_set = set()
	while currA:
		node_set.add(currA)
		currA = currA.next

	while currB:
		if currB in node_set:
			return currB
		currB = currB.next

	return None


# Approach 3
def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
	currA, currB = headA, headB
	lenA, lenB = 0, 0

	# get length of listA
	while currA:
		lenA += 1
		currA = currA.next

	# get length of listB
	while currB:
		lenB += 1
		currB = currB.next

	# if listA is longer
	if lenA > lenB:
		currA = headA
		while lenA != lenB:
			currA = currA.next
			lenA -= 1
		currB = headB

	# if listB is longer
	elif lenB > lenA:
		currB = headB
		while lenB != lenA:
			currB = currB.next
			lenB -= 1
		currA = headA

	while currA != currB or currA:
		currA = currA.next
		currB = currB.next
	else: return currA
