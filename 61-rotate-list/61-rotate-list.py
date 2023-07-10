# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # if there is no head
        if not head:
            return 
        #two variable to store length and tail
        length = 1
        tail = head
        
        # iterate till we have tail and find both tail and length
        while tail.next:
            tail = tail.next
            length += 1
        # take mod, so we dont do unneccessary iteration
        k = k % length
        
        # if k is multiple of length
        if k == 0:
            return head
        
        curr = head
        # iterating one less for pivot point
        for i in range(length - k - 1):
            curr = curr.next
        newhead = curr.next
        curr.next = None
        tail.next = head
        return newhead