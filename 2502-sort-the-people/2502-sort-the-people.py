class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
        zp = list(zip(names,heights))
        
        zp.sort(key= lambda x:x[1],reverse=True)
        
        t = 0
        for i in range(len(names)):
            e = zp[i]
            names[t] = e[0]
            t += 1
        return names