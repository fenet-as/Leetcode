class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        arr = [0]*3

        for e in nums:
            arr[e]+= 1
        
        t = 0
        for i,v in enumerate(arr):
            while v > 0:
                nums[t] = i
                v -= 1
                t += 1
            

        