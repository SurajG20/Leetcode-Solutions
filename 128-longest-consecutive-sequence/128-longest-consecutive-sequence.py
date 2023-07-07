class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numSets = set(nums)
        
        longest = 0
        
        for n in nums:
            # check if the number has any previous existance.
            if not (n-1) in numSets:
                length = 0 #current length of sequence
                while (n+length) in numSets:
                    length += 1
                longest = max(longest, length)

        return longest