class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = set()
        for c in s:
            if c not in count:
                count.add(c)
            else:
                count.remove(c) 
        return len(s) - len(count) +  1 if count else len(s)
        
        