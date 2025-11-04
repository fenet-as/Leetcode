class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        res = []
        nums.sort()

        for i,v in enumerate(nums):
            if v == target:
                res.append(i)
        return res
    