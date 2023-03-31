class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        l1 = [0]*10
        l2 = [0]*10
        bull = 0
        length = len(secret)
        nums1 = list(map(int, secret))
        nums2 = list(map(int, guess))
        
        print(nums1,nums2)
        for i in range(length):
            if nums1[i] == nums2[i]:
                bull += 1
            else:
                l1[nums1[i]] += 1
                l2[nums2[i]] += 1
            
        print(min(x,y) for x,y in zip(l1,l2))
        cows = sum(min(x,y) for x,y in zip(l1,l2))
        
        print(cows)
        return f"{bull}A{cows}B"
        
#         secret_dict = collections.defaultdict(int)
#         guess_dict = collections.defaultdict(int)

#         A, B = 0, 0
#         for i in range(len(guess)):
#             if secret[i] == guess[i]:
#                 A += 1
#             else:
#                 secret_dict[secret[i]] += 1
#                 guess_dict[guess[i]] += 1


#         for ele in guess_dict:
#             B += min(guess_dict[ele], secret_dict[ele])

#         result = '%dA%dB' % (A,B)
#         return result
        