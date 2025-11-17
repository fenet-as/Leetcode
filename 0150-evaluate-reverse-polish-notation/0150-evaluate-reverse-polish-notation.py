class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []

        for e in tokens:
            if e not in {'+','*','-','/'}:
                st.append(e)
            else:
                if len(st) >= 2:
                    fn = st.pop()
                    sn = st.pop()
                    if e == '+':
                        sm = int(fn)+int(sn)
                        st.append(sm)
                    elif e == '*':
                        pdt = int(fn)*int(sn)
                        st.append(pdt)
                    elif e == '/':
                        if fn == 0:
                            continue
                        else:
                            q = int(int(sn)/int(fn))
                            st.append(q)
                    elif e == '-':
                        m = int(sn)- int(fn)
                        st.append(m)
        
        return int(st[-1])
