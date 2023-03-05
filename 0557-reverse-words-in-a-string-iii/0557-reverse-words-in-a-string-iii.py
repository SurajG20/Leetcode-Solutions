class Solution:
    def reverseWords(self, s: str) -> str:
        temp = s.split(" ")
        res = []
        for n in temp:
            res.append(n[::-1])
            
        final = " ".join(res)
        return final