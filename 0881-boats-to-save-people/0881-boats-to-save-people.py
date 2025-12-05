class Solution:
    def numRescueBoats(self, nums: List[int], limit: int) -> int:
        '''
        people = [1,2], limit = 3
                  i j

        if n[i] + n[j] <= limit:
            ct += 1
            i += 1
            j -= 1
        elif n[i] + n[j] > limit:
            j -= 1

        [3,2,2,1]
        [1,2,2,3] ct = 1
           i   
           j

        '''
        
        nums.sort()
        i = 0
        j = len(nums)-1

        ct = 0

        while i < j:
            sm = nums[i] + nums[j]
            if sm <= limit:
                ct += 1
                i += 1
                j -= 1
            else:
                j -= 1
                ct += 1
        if i == j:
            ct += 1

        return ct


        