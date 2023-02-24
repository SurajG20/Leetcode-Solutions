*Explanation of this solution:*
​
The key is left = max(weights)
right = sum(weights),
which are the minimum and maximum possible weight capacity of the ship.
​
Therefore the question becomes Binary Search to find the minimum weight capacity of the ship between left and right.
We start from
mid = (left + right) / 2 as our current weight capacity of the ship.
days needed == 1
current load in the ship == 0
​
Start put load into ship in order.
when daysneeded > Days, it means the current ship is too small, we modify left = mid + 1 and continue
If all the currlaod is successfully put into ships, we might have a chance to find a smaller ship, so let right = mid and continue.
Finally, when our left == right, we reach our answer