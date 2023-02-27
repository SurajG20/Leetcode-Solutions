```
https://leetcode.com/problems/construct-quad-tree/discuss/404425/Python-solution-with-explanation.
​
#1. Iterate over all values in the current matrix. If all values are the same, return a new Node with val equals to the common value and isLeaf equals to True.
# 2.If not, we split the current matrix into 4 smaller square matrix and assign the returned root of the four recursive function to the topLeft, topRight, bottomLeft, bottomRight of the new root.
#3. Return the root.
```