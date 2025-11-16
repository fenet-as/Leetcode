class Solution:
    def clearDigits(self, s: str) -> str:
        st = []

        digits = {'0','1','2','3','4','5','6','7','8','9','10'}
        for e in s:
            if e in digits:
                if st:
                    st.pop()
            else:
                st.append(e)
            
        return ''.join(st)