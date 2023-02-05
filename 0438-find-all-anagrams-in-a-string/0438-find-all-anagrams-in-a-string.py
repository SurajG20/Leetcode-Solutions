class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # First we make a hashtable for p string
        # We compare this hashtable with hashtable of all substring of s

        res = [] # result 
        pCounter = Counter(p) # Counter for sting p
        sCounter = Counter(s[:len(p)-1]) # Counter for string s 
        
        for i in range(len(p)-1,len(s)):
            
            sCounter[s[i]] += 1   # include a new char in the window
            if sCounter == pCounter:    # This step is O(1), since there are at most 26 English letters 
                res.append(i-len(p)+1)   # append the starting index
            sCounter[s[i-len(p)+1]] -= 1   # decrease the count of oldest char in the window
            if sCounter[s[i-len(p)+1]] == 0:
                del sCounter[s[i-len(p)+1]]   # remove the count if it is 0
        return res
        