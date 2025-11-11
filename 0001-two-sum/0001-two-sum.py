class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}

        for i,v in enumerate(nums):
            if hm and target-v in hm:
                return [hm[target-v],i]
            hm[v] = i
