class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1]*len(nums1)
        stack = []
        map = {ele:idx for idx,ele in enumerate(nums1)}
        for num in nums2:
            while stack and num > stack[-1]:
                elem = stack.pop() 
                idx = map[elem]
                res[idx] = num
            if num in map:
                stack.append(num)          
        return res
                


