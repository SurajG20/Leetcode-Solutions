# So permutation of a string basically means just the reordering of the letters of the string. That means all the               # permutations of a string are just the anagrams of the string, with all the letters included, just in another way.
# And we have to find if such a substring exists in s2 which is a permutation of s1, which means we have to find a substring     # in s2 such that the frequency of the characters in that substring is same as the frequency of the characters in s1.

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        n1, n2 = len(s1), len(s2) # Length of s1 and s2 string               
                                                    
        ctr1, ctr2 = Counter(s1), Counter(s2[:n1])  # count the frequency for s1 and s2 (only till len of s1)
                                                    
        for i in range(n1,n2):    #Iterating through n1 to n2
            
            if ctr1 == ctr2: # Returns when both s1 and substring of s2 has same hash table
                return True           
            
            # Then we move the window
            ctr2[s2[i-n1]] -= 1    # Increment the intial element                   
            ctr2[s2[i]] += 1    # Add the element from behind 
            
        # When the last occurance does make them equal, we have to do this step
        return ctr1 == ctr2