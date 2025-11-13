class Solution:
    def scoreOfParentheses(self, s: str) -> int:

        '''
        "(())"

        if it opes and closes , i count score 1
        any nesting will be multipl of 2  
        '''

        st = []

        for e in s:
            if e == '(':
                st.append(e)
            else:
                if st and st[-1] == '(':
                    st.pop()
                    st.append(1)
                else:
                    st.append(e)

        ct = 0
        m = 1
        for e in st:
            if e == '(':
                m *= 2
            elif e == ')':
                m //= 2
            else:
                ct += m*e
        return ct

        