class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        '''
        "( ( ( ) ) ) ()"
        [o,o,1,c,c,1]

        sm = 5
        2 * 2
        1*4

        1
        sm += 1*1


        closing parenthesis

        - o -> 1
        - c/ >= 1 , c

        []

        '''


        ps = []

        st = []

        for e in s:
            if e == '(':
                st.append(e)
                ps.append('o')

            else:
                if ps:
                    if ps[-1] == 'o':
                        st.pop()
                        ps.pop()
                        ps.append(1)
                    elif ps[-1] == 1 or ps[-1] == 'c':
                        ps.append('c')
                        st.pop()
        

        sm = 0
        mf = 1
        for e in ps:
            if e == 'o':
                mf *= 2
            elif e == 'c':
                mf //= 2
            else:
                sm += mf*e
        return sm


