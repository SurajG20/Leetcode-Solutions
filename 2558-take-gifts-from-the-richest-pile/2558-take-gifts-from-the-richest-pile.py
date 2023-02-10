class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        # In python, we can only make min heap, thats why we negative the numbers
        gifts = [-x for x in gifts]
        
        
        # we make the heap of given list in O(N) time
        heapq.heapify(gifts)
        
        # we first remove the max(items), then take floor of sqare root of that number.
        # We need to take care of negative thing we did to the function
        
        while k:
            x = heapq.heappop(gifts)
            heapq.heappush(gifts,- floor(math.sqrt(abs(x))))
            k -= 1
            
        return - sum(gifts)
        