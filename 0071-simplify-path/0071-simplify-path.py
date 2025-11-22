class Solution:
    def simplifyPath(self, path: str) -> str:
        arr = path.split('/')

        stack = []

        for e in arr:
            if e == '..':
                if stack:
                    stack.pop()

            elif e == '.' or e == '':
                continue
            else:
                stack.append(e)

        
        res = '/' + '/'.join(stack)
        return res

