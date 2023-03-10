# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    import random

    def __init__(self, head: Optional[ListNode]):
        self.temp = []
        curr = head
        
        while curr:
            self.temp.append(curr.val)
            curr = curr.next
        self.last = len(self.temp)
    
    def getRandom(self) -> int:
        
        index = random.randint(0,self.last-1)
        
        return self.temp[index]


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()