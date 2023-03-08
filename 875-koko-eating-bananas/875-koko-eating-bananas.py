class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        res = max(piles) 
        while left <= right:
            mid = (left + right) // 2
            hours = 0
            # for b in piles:
            #     hours += math.ceil(b / mid)
            hours = sum(ceil(i/mid) for i in piles)
            if hours <= h:
                res = min(res,mid)
                right = mid - 1
            else:
                left = mid + 1
        return res
    
    
    # def minEatingSpeed(self, piles, H):
    #     beg, end = 0, max(piles)
    #     while beg + 1 < end:
    #         mid = (beg + end)//2
    #         if sum(ceil(i/mid) for i in piles) > H:
    #             beg = mid
    #         else:
    #             end = mid
                
    #     return end

