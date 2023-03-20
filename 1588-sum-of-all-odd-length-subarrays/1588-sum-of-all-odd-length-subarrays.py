class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        answer = 0
        
        for left in range(n):
            current_sum = 0
            for right in range(left, n):
                current_sum += arr[right]
                answer += current_sum if (right - left + 1) % 2 == 1 else 0
        return answer
        
        
        
        
#             def sum(x,y):
#                 total = 0
#                 for ele in range(x,y+1):
#                     total += arr[ele]

#                 return total
#             res = 0       
#             for i in range(len(arr)):
#                 for j in range(i,len(arr)):
#                     if (j - i )%2 ==0:
#                         res += sum(i,j)

#             return res


