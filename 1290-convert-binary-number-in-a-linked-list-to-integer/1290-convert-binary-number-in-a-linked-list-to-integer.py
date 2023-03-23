# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        
        res = 0
        temp = []
        while head:
            temp.append(head.val)
            head = head.next
        
        for i in range(len(temp)-1,-1,-1):
            res += temp[i]*(2**(len(temp)-1-i))
            
        return res