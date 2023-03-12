# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next
        if count == n :
            return head.next
        curr = head
        for i in range(1,count-n):
            curr = curr.next
        curr.next = curr.next.next
        return head
        
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
	
	    fast = slow = head
	    for i in range(n):
		    fast = fast.next
	    if not fast: return head.next
	    while fast.next:
		    fast, slow = fast.next, slow.next
	    slow.next = slow.next.next
	    return head      