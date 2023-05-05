class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        l = 0
        count = 0
        res = 0
        
        vowelSets = {'a','e','i','o','u'}
        for r in range(len(s)):
            if s[r] in vowelSets:
                count += 1
                
            if r - l + 1 > k:
                count -= 1 if s[l] in vowelSets else 0
                l += 1
            
            res = max(count,res)
        return res                