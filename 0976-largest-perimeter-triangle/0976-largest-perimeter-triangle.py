class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:


        nums.sort()
        j = len(nums)-1
        while j-2 >= 0:
            s1 = nums[j]
            s2 = nums[j-1]
            s3 = nums[j-2]

            if s1 < (s2+ s3):
                return s1+s2+s3
            j -= 1
        return 0