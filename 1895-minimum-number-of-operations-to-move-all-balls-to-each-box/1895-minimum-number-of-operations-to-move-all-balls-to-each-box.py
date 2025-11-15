class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        
        lm = [0]*len(boxes)

        ct = 0
        mvs = 0
        for i in range(len(boxes)):
            lm[i] = mvs
            ct += int(boxes[i])
            mvs += ct

        rm =[0]*len(boxes)
        ct = 0
        mvs = 0

        for i in range(len(boxes)-1,-1,-1):
            rm[i] = mvs
            ct += int(boxes[i])
            mvs += ct
        
        res = []
        
        for i in range(len(boxes)):
            res.append(rm[i]+lm[i])
        return res

