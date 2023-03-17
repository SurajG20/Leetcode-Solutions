class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Put all elements into a priority queue.
        # Pop out the two biggest, push back the difference,
        # until there are no more two elements left.
        if len(stones) == 1:
            return stones[0]
        stones = [-x for x in stones]
        heapify(stones)
        while len(stones) > 1:
            x = heappop(stones)
            y = heappop(stones)
            if x != y:
                heappush(stones,x-y)
        return -stones[0] if len(stones)==1 else 0
        