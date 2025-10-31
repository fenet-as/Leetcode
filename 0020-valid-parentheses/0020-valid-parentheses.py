class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        

        for e in s:
            if e in "([{":
                st.append(e)
            else:
                if st:
                    if e == "]" and st[-1] == "[":
                        st.pop()
                    elif e == "}" and st[-1] == "{":
                        st.pop()
                    elif e == ")" and st[-1] == "(":
                        st.pop()
                    else:
                        return False
                else:
                    return False
        if not st:
            return True
        return False