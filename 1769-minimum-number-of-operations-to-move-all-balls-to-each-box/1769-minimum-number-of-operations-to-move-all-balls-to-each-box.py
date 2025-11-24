class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        oi = []

        for i in range(len(boxes)):
            if boxes[i] == '1':
                oi.append(i)
            
        res = []

        for i in range(len(boxes)):
            ct = 0
            for e in oi:
                if e != i:
                    ct += abs(e-i) 
            res.append(ct)
        return res

