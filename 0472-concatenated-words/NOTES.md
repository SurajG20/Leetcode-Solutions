​
1. Create an empty set 's' to store all the words in the given array of strings.
2. Iterate through the array of strings and insert each word into the set 's'.
3. Create an empty vector 'concatenateWords' to store all the concatenated words.
4. Iterate through the array of strings again, for each word, check if it is a concatenated word using the function 'checkConcatenate(word)'.
5. In the 'checkConcatenate(word)' function, use a for loop to iterate through each substring of the word, starting from index 1 to the second last index of the word.
6. For each substring, check if the prefix and suffix of the substring exists in the set 's'.
7. If the prefix and suffix both exist in the set 's', then return true, indicating that the word is a concatenated word.
8. If the function 'checkConcatenate(word)' returns true, then insert the word into the 'concatenateWords' vector.
9. Return the 'concatenateWords' vector.
​
![](https://assets.leetcode.com/users/images/d47869df-216b-4184-a650-00035a86e96c_1674785146.2162044.jpeg)