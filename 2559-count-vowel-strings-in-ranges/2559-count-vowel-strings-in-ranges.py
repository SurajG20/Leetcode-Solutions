class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        
        # This range type problem can be solved using prefix sum. We help in make it linear, First we create an array with word being vowels eligible by boolean value.
        
        prefix_sum = [0] # We add 0 intially in prefix_sum array because it shows what is sum till this index.
        
        sum = 0
        for word in words:
            if word[0] in "aeiou" and word[-1] in "aeiou":
                sum += 1
            prefix_sum.append(sum)
        res = []
        
        for l,r in queries:
            res.append(prefix_sum[r+1]-prefix_sum[l])
        return res
        
class Solution:
    
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        
        # we can do this same problem with accumulate function to create prefix sum
        
                                                                # Example:
                                                                #    words = ['aba','bcb','ece','aa','e'] 
                                                                #  queries = [[0,2], [1,4], [1,1]]

        vowels = lambda w: w[0] in 'aeiou' and w[-1] in 'aeiou' #  <-- boolean function  

        words = map(vowels, words)                              #    words = [True, False, True, True, True]
        
        pref = list(accumulate(words, initial = 0))             #     pref = [0, 1, 1, 2, 3, 4]
        
        return [pref[r+1] - pref[l] for l,r in queries]         #   return [2-0, 4-1, 1-1] = [2,3,0]      
    
    
#         # This solution will not work because of quadratic time complexity.
#         # map for vowels
#         map = {"a","e","i","o","u"}
        
#         def isvowel(w): # A function to tell if a word is vowel
#             if w[0] in map and w[-1] in map:
#                 return True
#             else:
#                 return False
            
#         res = []  # result
        
#         for q in queries:
            
#             sum = 0 # initialising sum
            
#             for j in range(q[0],q[1]+1):
                
#                 if isvowel(words[j]):
#                     sum += 1
                    
#             res.append(sum)
            
#         return res
            