class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        
        ones = []

        for i in range(len(boxes)):
            if boxes[i] == '1':
                ones.append(i)
        
        res = []
        for i in range(len(boxes)):
            sm = 0
            for e in ones:
                if e != i: 
                    sm += abs(e-i)
            res.append(sm)

        return res

