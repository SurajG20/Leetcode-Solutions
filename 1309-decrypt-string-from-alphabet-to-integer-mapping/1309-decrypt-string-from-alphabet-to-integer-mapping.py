class Solution:
    def freqAlphabets(self, s: str) -> str:
        hashmap = {}        
        for idx,letter in enumerate(string.ascii_lowercase):
            hashmap[idx+1] = letter
         
        print(hashmap)
        res = ''
        
        i = len(s) - 1
        while i >= 0:
            if s[i] != '#':
                res += hashmap[int(s[i])]
                i -= 1
            else:
                temp = s[i-2] + s[i-1]
                res += hashmap[int(temp)]
                i -= 3
                
        return res[::-1]
                
            