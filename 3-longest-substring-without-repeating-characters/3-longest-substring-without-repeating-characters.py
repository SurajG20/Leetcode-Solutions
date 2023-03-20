class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in hash:
                hash.remove(s[l])
                l += 1
            hash.add(s[r])
            res = max(res, len(hash))
            
        return res
        
