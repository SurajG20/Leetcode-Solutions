Left pointer is where the next 0 will be at
Right pointer is where the next 2 will be at
​
"Iterate" through the list from left to right (Before reaching the latest "2" that has been swapped)
If the number is a 2, swap with the right pointer number and decrement it by one (As the next 2 will be to the left of the swapped "2")'
Elif the number is a 0, similarly, swap with the left pointer number and increment it by one.
Else (If the number is a 1), just "skip" the number
​