*Intuition of this Problem:*
​
The intuition behind this logic is to reduce the maximum difference between any two elements in the array by either decreasing the maximum value or increasing the minimum value.
​
By transforming all odd numbers to even numbers, we can always divide even numbers by 2, so the maximum value in the array can be reduced to its minimum possible value. We also keep track of the minimum value in the array, since we can only increase it by multiplying it by 2.
​
We then repeatedly pop the maximum value from the priority queue, which guarantees that we are always reducing the maximum value in the array. If the maximum value is odd, we can no longer divide it by 2, so we break out of the loop. Otherwise, we divide the maximum value by 2, which reduces the maximum value, and update the minimum value accordingly.
​
By doing this repeatedly, we can always reduce the maximum difference between any two elements in the array, and we keep track of the minimum deviation that we can achieve