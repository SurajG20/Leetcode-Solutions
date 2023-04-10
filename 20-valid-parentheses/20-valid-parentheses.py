class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {'}':'{',')':'(',']':'[',}
        stack = []
        for c in s:
            if stack and c in brackets:
                if stack[-1] != brackets[c]:
                    return False
                else:
                    stack.pop()
            else:
                stack.append(c)
        return stack == []

        # brackets = {"]":"[","}":"{",")":"("}  #creating a dictionary to check the occurance of closing brackets
        # stack = [] # an empty list to store the opening bracket
        # for c in s: #iterating over the string, checking all the character
        #     if stack and c in brackets: #if the character is in the dictionary
        #         if stack[-1] != brackets[c]: #if the stack is not empty and last stored value in the stack is not equel to corresponding element of character in the dictionary
        #             return False #then return false
        #         else:
        #             stack.pop() #if it matches then pop the element from the stack
        #     else:
        #         stack.append(c) #if it is a opening brackets then just add the bracket in the list
        # return stack == []  #check if the list is empty or not

        