class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''
        - sort position in reverse order, zip with speed
        - calculate time (tgt - p)/v
        [1,1,12,]
        - st[]
        if e > st[-1]:
            f += 1


        '''

        arr = list(zip(position,speed))
        arr.sort(key=lambda x:x[0], reverse = True)
        
        t = []

        for e in arr:
            ct = (target - e[0])/e[1]
            t.append(ct)
        
        st = []
        
        for e in t:
            if st and e <= st[-1]:
                continue
            
            st.append(e)
        return len(st)
        