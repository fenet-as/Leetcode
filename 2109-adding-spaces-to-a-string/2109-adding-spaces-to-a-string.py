class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = []
        pi = 0
        for i in spaces:
            res.append(s[pi:i])
            pi = i
            
        res.append(s[pi:])
        
        return ' '.join(res)
