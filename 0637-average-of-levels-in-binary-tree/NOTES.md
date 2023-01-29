---> In this problem we need to traverse tree, using either bfs of dfs and for each node we need to calculate its level.
=== Using BFS ===
​
1. First, we put root into our queue (using deque python library).
2. On each iteration we extract all nodes from queue from the left and put all children to the rigtht. In this way on each step we will have one full level.
3Evaluate average of elements in list and add it to final result.