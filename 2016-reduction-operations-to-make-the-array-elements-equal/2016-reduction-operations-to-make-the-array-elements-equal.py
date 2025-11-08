from collections import Counter

class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        '''
        loop over the arr , find max
        loop and find the 2nd 

        -- counter : counts the ocuurunce of each element
        # sort the unique elements

        [5,1,3]
        hold the min value
        loop over the array and using the counter we count the number opeartion
        [1,1,2,2,3]
        # create set of array
        iterate over the dictionary
        construct a uniques array
        

        1:2
        2:2
        3:1

        [1,7,7,7,7,8,8,8,8,9,44]
        1:1
        7:4
        8:4
        9:1
        44:1
        1+ 2 +6 + 10 +

        iterate backwards ct * ind
        1 * 2 = 2
        2 * 1 = 2
        2 * 0 = 0


        ct = Counter(nums)

        ua = []
        

        for e in ct:
            ua.append(e)

        opc = 0
        for i in range(len(ua)):
            r = ct[ua[i]] * i
            opc += r
        
        

        '''
        ct = Counter(nums)

        ua = []
        

        for e in ct:
            ua.append(e)
        ua.sort()

        opc = 0
        for i in range(len(ua)):
            r = ct[ua[i]] * i
            opc += r

        return opc

