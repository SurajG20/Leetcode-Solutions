class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        
        map = defaultdict(int)
        
        for ch in s:
            map[ch] += 1
            
        print(map)
        res = ""
        for ch in t:
            if ch not in map:
                res += ch
            else:
                map[ch] -= 1
                
                if map[ch] == 0:
                    del map[ch]
        return res
                