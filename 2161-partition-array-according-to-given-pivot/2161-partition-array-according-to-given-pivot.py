class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        
        res = []

        for e in nums:
            if e < pivot:
                res.append(e)
        
        for e in nums:
             if e == pivot:
                res.append(e)
        for e in nums:
            if e > pivot:
                res.append(e)

        return res