```
# Solution approach:- Use DFS traversal(Recursive DFS) first go to left and then go to right.
# 0) If the root node is only one the node which you are looking for then return root
# 1) If both left and right returns null then returns null
# 2) If left returns a node and right returns null then return left and vice versa (Return something which gives u node)
# 3) If both returns you the nodes then u have found the answer so return root
Time: O(N), where N is number of nodes in the Binary Tree.
Space: O(H), where H is the heigh of Binary Tree.
```