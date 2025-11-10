class Solution:
    def generate(self, numRow: int) -> List[List[int]]:
        '''
        [1,2,1]
        [1,3,3,1]
        [1,4,6,4,1]

        '''
        res = [[1],[1,1],[1,2,1]]

        if numRow == 1:
            return [[1]]
        elif numRow == 2:
            return [[1],[1,1]]
        elif numRow == 3:
            return [[1],[1,1],[1,2,1]]
        
        while len(res) < numRow:
            la = res[-1]
            na = [1]
            for i in range(len(la)-1):
                na.append(la[i]+la[i+1])
            na.append(1)
            res.append(na)
        return res
        
        