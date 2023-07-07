*1. This approach is very intuitive and easy to get.*
​
1.  We just iterate in the first-pass to find the length of the linked list - len.
​
2.  In the next pass, iterate len - n - 1 nodes from start and delete the next node (which would be nth node from end).
​
*2. We are required to remove the nth node from the end of list. For this, we need to traverse N - n nodes from the start of the list, where N is the length of linked list. We can do this in one-pass as follows -
*
1.  Let's assign two pointers - fast and slow to head. We will first iterate for n nodes from start using the fast pointer.
​
2.   Now, between the fast and slow pointers, there is a gap of n nodes. Now, just Iterate and increment both the pointers till fast reaches the last node. The gap between fast and slow is still of n nodes, meaning that slow is nth node from the last node (which currently is fast).
​
**For eg**. let the list be 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9, and n = 4.
​
1. 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> null
^slow               ^fast
|<--gap of n nodes-->|
=> Now traverse till fast reaches end
2. 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8 -> 9 -> null
^slow               ^fast
|<--gap of n nodes-->|
'slow' is at (n+1)th node from end.
So just delete nth node from end by assigning slow -> next as slow -> next -> next (which would remove nth node from end of list).
​
-----.>  Since we have to delete the nth node from end of list (And not nth from the last of list!), we just delete the next node to slow pointer and return the head.
​
​