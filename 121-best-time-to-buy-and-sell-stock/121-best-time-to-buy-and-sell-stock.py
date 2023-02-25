class Solution:
    def maxProfit(self, prices: List[int]) -> int:
#         max_profit = 0
#         for i in range(len(prices)):
#             for j in range(i,len(prices)):
#                 if prices[j] >= prices[i]:
#                     max_profit = max(max_profit,prices[j]-prices[i])
                    
#         return max_profit

        left = 0
        right = 1
        
        max_profit = 0
        
        while right < len(prices):
            current_profit = prices[right] - prices[left]
            if prices[right] > prices[left]:
                max_profit = max(max_profit, current_profit)
            else:
                left = right
            right += 1
        return max_profit
        