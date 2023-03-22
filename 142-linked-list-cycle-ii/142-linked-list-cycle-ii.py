# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        lookup = set()
        
        while curr:
            if curr in lookup:
                return curr
            lookup.add(curr)
            curr = curr.next
        return None
#         # both pointer start from head
#         slow, fast = head, head
        
#         # till fast is not None
#         while fast and fast.next:
            
#             # slow pointer moves one step, while fast pointer move two step
#             slow = slow.next
#             fast = fast.next.next
            
#             # if they become equal means there is cycle 
#             if slow == fast:
                
#                 # we reset slow pointer
#                 slow = head
                
#                 # kept fast as it is, untill they do not collab
#                 # there is mathematical reason behind it 
#                 while slow != fast:
#                     slow = slow.next
#                     fast = fast.next
#                 return slow


