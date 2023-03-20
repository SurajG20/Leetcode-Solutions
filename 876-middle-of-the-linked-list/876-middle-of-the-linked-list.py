# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # curr = head
        # n = 0
        # while curr:
        #     n += 1
        #     curr = curr.next
        # for i in range(n//2):
        #     head = head.next
        # return head
    
        slow,fast = head,head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow
        
        