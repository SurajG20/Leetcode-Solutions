```
# O(n) because we iterate over nums once, then inside that loop, we
# pop the stack an aggregated maximum of n times over the lifetime
# of the outer loop
​
from collections import deque
​
​
class Solution:
def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
# will contain TreeNodes in monotonically decreasing order of "val"
stack = deque()
​
for num in nums:  # O(n)
node = TreeNode(num)
# while the top of the stack is < num, pop it and put it on the left
# run time: each element is only appended to stack once, so inner
# loop can't have more than n total iterations, so this is another O(n)
while stack and stack[-1].val < num:
# we don't care about losing nodes b/c the max value node
# is at the bottom of the stack and is continuously mutated
# via mutations to its child nodes
node.left = stack.pop()
# at this point we know that the top of the stack is
#  a. to the left of num in the nums array
#  b. greater than num
# so we know num should be in its right leaf
if stack:
stack[-1].right = node
# retain monotonically decreasing order,
# we know node.val is < the val of the top of the stack
stack.append(node)
return stack[0]
```
https://leetcode.com/problems/maximum-binary-tree/discuss/258364/Python-O(n)-solution-with-explanation.
​
https://leetcode.com/problems/maximum-binary-tree/discuss/316286/Python-O(n)-Solution-with-explanation