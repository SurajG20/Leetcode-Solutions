class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        hashmap = {}
        
        for key, val in enumerate(s):
            if val in hashmap:
                hashmap[val] += 1
            else:
                hashmap[val] = 1
                
        for ch in range(len(s)):
            if hashmap[s[ch]] == 1:
                return ch
        return -1