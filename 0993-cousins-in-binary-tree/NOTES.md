Two nodes of a binary tree are cousins if they have the same depth with different parents.
​
First thing we have in mind is that we have to keep track of both parent and depth of each node.
​
We can have both iterative and recursive solution.
​
Iterative ->
​
*  we can have one queue, with node and its parent as its value.
*  for each node, we check if they are x and y because every node is distinct.
*  we make two variable xparent and yparent.. if any node matches, we change the value of both variable.
*  check if both are same or not. we dont have to check for level, as it is a queue
*  We then just have to append node.left and node.right
​
Recursive->
* we make same variables- xdepth,  ydepth , xparent,  yparent
* we have to keep track of depth.
* we make dfs call- node, parent, x , y, depth. start with root.
* we check if this node is x or y, and keep track of their depth and parent
* in the end, check if they have same depth but different parent
​
​
​
​
*The idea is to traverse our tree with function dfs(node, par, dep, val), where:*
​
* node is current node we are in.
* par is parent of node, we need it in the end to check that nodes have different parents.
* dep is depth of node, in the beginning depth of root is equal to 0.
* val is value we are looking for.
* Now, we run dfs(root, None, 0, x) and similar logic for y and we use the logic inside:
​
>>> if not node:
return means that we reached None node.
>>> if node.val == val, it means that we found node with desired value, we return dep, par for this node.
>>> We run function recursively for the left and for the right children. Then we use or which will take value from the branch which have desired node.
*Complexity*
It is O(n) for time and O(h) for space.