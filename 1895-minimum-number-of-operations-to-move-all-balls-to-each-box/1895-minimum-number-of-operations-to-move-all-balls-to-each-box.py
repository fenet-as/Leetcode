class Solution:
    def minOperations(self, boxes: str) -> List[int]:

        '''
        prepare 1 array
        for each index go through the 1 index array and 
        keep ct of operations 
        append that op to res

        '''
        hm = []
        for i in range(len(boxes)):
            if boxes[i] == "1":
                hm.append(i)
        
        res = []
        
        for i in range(len(boxes)):
            ct = 0
            for j in range(len(hm)):
                ct += abs(hm[j] - i)
            res.append(ct)
        

        return res

