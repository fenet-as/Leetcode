class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()

        i = 0
        sm = 0
        while i < len(nums):
            sm += nums[i]
            i += 2
        return sm