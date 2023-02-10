class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        
        # TC - O(N + klogN)
        # SC - O(N)
        # We have piles of stone in the from an array
        # we have to make minimum number of stone possible to it, hence we have to make number of stone each time.
        
        piles = [-x for x in piles]
        
        heapq.heapify(piles)
        
        while k:
            curr = - heapq.heappop(piles)
            remove = curr//2
            heapq.heappush(piles, -(curr - remove))
            k -= 1
            
        return - sum(piles)
    
        