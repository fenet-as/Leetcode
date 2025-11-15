class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        
        while len(nums) > 1:
            for i in range(len(nums)-1):
                sm = (nums[i] + nums[i+1]) % 10
                nums[i] = sm
            nums.pop()

        return nums[0]