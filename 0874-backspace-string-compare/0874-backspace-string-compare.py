class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        st1 = []
        st2 = []

        for e in s:
            if e == "#":
                if st1:
                    st1.pop()
            else:
                st1.append(e)
        
        for e in t:
            if e == "#":
                if st2:
                    st2.pop()
            else:
                st2.append(e)
        return st1 == st2
