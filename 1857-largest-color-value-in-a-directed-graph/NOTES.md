**Idea**
​
The main idea is if there is a path with max. frequency of the color, then we can take any path containing it without changing the frequency of the max. color. Thus, we only need to count the colors along the longest possible paths.
The composition of the colors along each of the paths does not matter. We only need to count max. frequency of each of the colors along all the paths that lead to the terminal node.
​
**Algorithm**
​
For each node (starting from the nodes that do not have incoming edges), calculate how frequent each of the colors is along all possible paths that lead to that node. Update max. for the outgoing nodes. We can process each node as soon as we process all the incoming nodes/edges for the node.
​
**Variables**
​
Graph contains graph coding - the list of outgoing edges for each node.
incoming contains the number of unprocessed incoming edges for the node. The number is changing as we process edges. If an incoming edge is processed, then we decrement incoming counter for the node.
stack contains the current list of nodes to process. For all the nodels in stack, we have already processed all the incoming edges.
cnts - the count of the frequency of all the colors for the paths that lead to the node. We increment the color of the node itself when we pop the node from the queue.