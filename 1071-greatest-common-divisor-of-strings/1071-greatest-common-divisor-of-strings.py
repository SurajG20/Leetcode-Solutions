class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        
        # 1. Find the shorter string among str1 and str2, without loss of generality, let it be str1.

        # 2. Start with base = str1, and check if both str1 and str2 are made of multiples of base.

        # 3. If so, return base.
        # 4. Otherwise, we shall try a shorter string by removing the last character from base.
        # 5. If we have checked all prefix strings without finding the GCD string, return "".

        N = len(str1)
        M = len(str2)
        K = min(N,M)
        for L in range(K,0,-1):
            if K % L != 0:
                continue
            s = str1[:L]
            
            copies = N // L
            if s * copies != str1:
                continue
            
            copies2 = M//L
            if s * copies2 != str2:
                continue
            
            return s
        return ""
                
# class Solution:
#     def gcdOfStrings(self, str1: str, str2: str) -> str:
#         len1, len2 = len(str1), len(str2)
        
#         def valid(k):
#             if len1 % k or len2 % k: 
#                 return False
#             n1, n2 = len1 // k, len2 // k
#             base = str1[:k]
#             return str1 == n1 * base and str2 == n2 * base 
        
#         for i in range(min(len1, len2), 0, -1):
#             if valid(i):
#                 return str1[:i]
#         return ""