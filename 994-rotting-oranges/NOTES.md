The dfs will not work here, because we to check for every rotten oragnes simultaneously.
hence we will use bfs.
we make a queue for bfs search. -- > Multi Sources bfs.
​
To ensure that all fresh oranges are rotten, we wil keep track of oranges.
​
and also append all rotten apples to a queue
​
make a directions array.
to keep track of all directions
while there is elements in queue we keep popping them and check for all directions, only if they are eligible. and mark it as rotten. and append it queue.
decrement fresh oranges
increase time for one loop
​
return time
​