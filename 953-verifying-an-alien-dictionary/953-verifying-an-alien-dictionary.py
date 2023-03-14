class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # To check if words are sorted, we keep comparing for adjacents words. 
        # Its easy to compare words in pair, instead of all at a time
        
        map = {}
        
        # We store the letter - order, we can easily access order when we compare them.
        for i in range(len(order)):
            map[order[i]] = i + 1 
        print(map)
        
        # To compare two adjacent words words[i] and words[i+1], we want to find the first letter that is different:
        # if words[i] has the lexicographically smaller letter, then we can exit from the iteration because we know
        # words[i] and words[i+1] are in the right order; however, if words[i] has the lexicographically larger 
        # letter, then we immediately return false, because we found one pair of words that are in the wrong order.
        
        for i in range(len(words)-1):
            print("i",i)
            for j in range(len(words[i])):
                print("j",j)
                if j >= len(words[i+1]):
                    return False
                print("1",words[i][j])
                print("2",words[i+1][j])
                if words[i][j] != words[i+1][j]:
                    if map[words[i][j]] > map[words[i+1][j]]:
                        return False
                    break
        return True 
                    
                
            
         