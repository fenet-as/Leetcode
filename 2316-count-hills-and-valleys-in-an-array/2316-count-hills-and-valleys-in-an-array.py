class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        '''
        [5,7,7,1,7]
                 i
        '''
        
        ul = []

        n = len(nums)

        for i in range(n-1):
            if nums[i] != nums[i+1]:
                ul.append(nums[i])
        ul.append(nums[n-1])


        i = 0
        j = 1
        k = 2
        ct = 0
        while k < len(ul):
            if ul[j] < ul[k] and ul[j] < ul[i]:
                ct += 1
            elif ul[j] > ul[k] and ul[j] > ul[i]:
                ct += 1
            i += 1
            j += 1
            k += 1
        return ct 



