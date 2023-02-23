class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        maxProfitHeap = []

        # Insert all capitals to a min-heap
        minCapitalHeap = [(capital[i],i) for i in range(len(capital))]
        heapq.heapify(minCapitalHeap)
        
        # Finding 'k' best projects
        availableCapital = w
        for _ in range(k):
            # Projects that can be selected within the available capital. Insert these in a max-heap
            while minCapitalHeap and minCapitalHeap[0][0] <= availableCapital:
                capital, i = heappop(minCapitalHeap)
                heappush(maxProfitHeap, -profits[i])

            # Break if we are not able to find any project that can be completed within the available capital
            if not maxProfitHeap:
                break

            # Add the profit from project with the maximum profit
            availableCapital += -heappop(maxProfitHeap)

        return availableCapital