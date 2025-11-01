class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        st = []
        sol = [0] * len(t)

        for i in range(len(t)-1,-1,-1):
            while st and t[st[-1]] <= t[i]:
                st.pop()
            if st:
                sol[i] = st[-1] - i
            
            st.append(i)
        return sol
        
            
