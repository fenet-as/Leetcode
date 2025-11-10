from collections import Counter
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []

        hm = Counter(nums1)

        st = set(nums2)
        for e in st:
            if e in hm:
                res.append(e)
        return res
