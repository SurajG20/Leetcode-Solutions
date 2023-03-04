class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        p1 = 0
        p2 = 0
        
        r = []
        while p1 < len(nums1) and p2 < len(nums2):
            val1 = nums1[p1]
            val2 = nums2[p2]
            if val1 == val2:
                r.append(val1)
                p1 += 1
                p2 += 1
            elif val1 < val2:
                p1 +=1
            elif val1 > val2:
                p2 += 1
                
        return r  