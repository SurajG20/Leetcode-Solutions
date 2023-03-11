# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = curr = ListNode() # create a dummy node
        stack = [] # empty stack to store data
        # append all node to an stack
        while head:
            stack.append(head.val)
            head = head.next
        # while poping element we store create a node with them
        while stack:
            curr.next = ListNode(stack.pop())
            curr = curr.next
        return dummy.next


        
#     def reverseList(self, head: ListNode) -> ListNode:
#         if not head or not head.next:
#             return head
#         node = self.reverseList(head.next)
#         head.next.next = head
#         head.next = None
#         return node
