class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        '''

        mx = 18

        res = [17     ,6,6,1,-1]
        '''


        mx = -1
        res = [0] * len(arr)
        for i in range(len(arr)-1,-1,-1):
            res[i] = mx
            mx = max(mx,arr[i])
        
        return res
            
            