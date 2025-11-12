class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        

        j = 0
        mx = 0
        while j < len(nums):
            ct = 0
            while  j < len(nums) and nums[j] == 1:
                ct += 1
                j += 1
            mx = max(ct,mx)
            j += 1
        return mx

