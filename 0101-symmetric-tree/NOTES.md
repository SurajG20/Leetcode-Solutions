---> We need to validate only 3 conditions including base condition and recursively call to the function:
​
*   If both "leftRoot" and "rightRoot" are null, return true
*   If only one of "leftRoot" or "rightRoot" is null, return false
*   If "leftRoot" and "rightRoot" are not null and their values are not equal, return false
*   If "leftRoot" and "rightRoot" are not null and their values are equal, recursively call "isTreeSymmetric" on the left child of "leftRoot" and the right child of "rightRoot", and the right child of "leftRoot" and the left child of "rightRoot"
​
``def isSymmetric(self, root):
if not root:
return True
return self.dfs(root.left, root.right)
def dfs(self, l, r):
if l and r:
return l.val == r.val and self.dfs(l.left, r.right) and self.dfs(l.right, r.left)
return l == r
def isSymmetric(self, root):
if not root:
return True
stack = [(root.left, root.right)]
while stack:
l, r = stack.pop()
if not l and not r:
continue
if not l or not r or (l.val != r.val):
return False
stack.append((l.left, r.right))
stack.append((l.right, r.left))
return True```
​