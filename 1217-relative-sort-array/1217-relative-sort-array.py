class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        '''
        left out arrays collect
        common array count
        
        '''
        la = []
        ct = defaultdict(int)
        for e in arr1:
            if e not in arr2:
                la.append(e)
            else:
                ct[e] += 1
        
        res = []
        for e in arr2:
            for _ in range(ct[e]):
                res.append(e)
        la.sort()
        res.extend(la)
        return res
        

