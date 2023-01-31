# Approach for this Problem:
1. Create a pair array of size n where n is the size of scores and ages arrays.
2. Store each player's score and age as a pair in the above array.
3. Sort the pair array in increasing order of age.
4. Initialize an array dp of size n and set dp[i] to be the score of player i for all 0 <= i < n.
5. Initialize a variable ans to store the maximum overall score.
6. Loop through the pair array from index i = 0 to i = n - 1.
7. For each i, loop through j from 0 to i - 1.
8. If the score of player j is less than or equal to the score of player i, update dp[i] to be the maximum of dp[i] and dp[j] + score[i].
9. Set ans to be the maximum of ans and dp[i].
10. Return ans as the result.