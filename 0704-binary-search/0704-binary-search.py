class Solution:
    def search(self, nums: List[int], target: int) -> int:
        

        '''
        while i <= j
        mi = i + j//2
        if mi
        '''

        i = 0
        j = len(nums)-1

        while i <= j:
            mi = (i+j)//2

            

            if nums[mi] == target:
                return mi
            elif nums[mi] < target:
                i = mi + 1
            else:
                j = mi-1
        return -1