​
*  If we have value in node higher than high, then we need to cut this node and its right children (because it is BST), so we just return dfs(node.left).
*  Similarly if value is less than low, we return dfs(node.right).
*  Finally, if it is in between, we need to attach dfs(node.left) as left children and dfs(node.right) as right children and return our node, exactly this is meant by phrase "Trimming the tree should not change the relative structure of the elements that will remain in the tree". So, if we need to delete some node, we need to reattach its children to its parent.
*  you will never need to cut middle of the tree, see [4, 2, 5, 1, 3] tree, it is not possible to cut 2 out of this tree with keeping its stucture, because then root 4 must have 3 children. However it will never be the case, because if we need to cut 2 from tree, we either need to cut all number more than 2, or all numbers less than 2
​