class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        arr = []
        
        for x in accounts:
            arr.append(sum(x))
        return max(arr)