class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a = [0]*3

        for e in nums:
            a[e] += 1
        
        t = 0
        for i in range(3):
            while a[i] > 0:
                nums[t] = i
                a[i] -= 1
                t += 1
        

