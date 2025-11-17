class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        st = set(arr2)
        hm = defaultdict(int)
        nue = []
        for e in arr1:
            if e not in st:
                nue.append(e)
            else:
                hm[e] += 1
        
        res = []

        for e in arr2:
            for _ in range(hm[e]):
                res.append(e)
        if not nue:
            return res 
         

        mx = max(nue)

        ca = [0]*(mx+1)

        for e in nue:
            ca[e] += 1
        
        t = 0
        for i in range(len(ca)):
            while ca[i] > 0:
                nue[t] = i
                t += 1
                ca[i] -= 1
        

        res.extend(nue)
        return res            

        

            