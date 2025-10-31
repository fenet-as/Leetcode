class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        '''
        

        '''

        sol = [0] * len(t)
        st = []

        for i in range(len(t)-1,-1,-1):
            while st and t[i] >= t[st[-1]]:
                st.pop()
            if st:
                sol[i] = st[-1]-i
            st.append(i)
        
        return sol
            
