class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hm = {}

        for i,v in enumerate(nums):
            if v in hm and abs(hm[v] - i) <= k:
                return True
            hm[v] = i
        return False
        
