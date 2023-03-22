class Solution:
    def interpret(self, command: str) -> str:
        map = {"G":"G","()":"o","(al)": "al"}
        
        res = ""
        temp = ""
        
        for i in range(len(command)):
            temp += command[i]
            
            if temp in map:
                res += map[temp]       
                temp = ""
                
        return res
            