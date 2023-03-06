For a >= b >= c, a,b,c can form a triangle if a < b + c.
​
We sort the A.
* Try to get a triangle with 3 biggest numbers.
* If A[n-1] < A[n-2] + A[n-3], we get a triangle.
* If A[n-1] >= A[n-2] + A[n-3] >= A[i] + A[j], we cannot get any triangle with A[n-1]
* repeat step2 and step3 with the left numbers.