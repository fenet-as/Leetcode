class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st1 = set(nums2) # O(n2)
        
        res = set() #O(k)
        for e in nums1: #O(n1)
            if e in st1:
                res.add(e)
        
        r = list(res) #O(k)
        return r
