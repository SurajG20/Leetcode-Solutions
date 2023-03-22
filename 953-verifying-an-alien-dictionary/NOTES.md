1. To check if words are sorted, we keep comparing for adjacents words.
2. Its easy to compare words in pair, instead of all at a time
3. To compare two adjacent words words[i] and words[i+1], we want to find the first letter that is different:
4.  if words[i] has the lexicographically smaller letter, then we can exit from the iteration because we know
5.  words[i] and words[i+1] are in the right order; however, if words[i] has the lexicographically larger
6.  letter, then we immediately return false, because we found one pair of words that are in the wrong order.
​
​
>>>> We also need to consider the boundaries. <<<<<
While we loop from the beginning to the end of one word, we need to check if the other word has ended. we reach the end of one word before finding the first different letter.
When this happens, we must examine the length of each word:
1. if the words are the same length or the former word is shorter, then words is sorted.
2.  if the latter word is shorter, then words is not sorted.