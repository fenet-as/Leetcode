class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        '''
        ((()()))
        ['o', 'o', 1, 1, 'c', 'c']
        2 * 2 * ( 1 + 1) 
        4 (1 + 1)
        4 + 4
        m = 4
        sc = 4 + 4
        
        oo2 - 
        11
        o1
        1
        oo11

        
        '''
        n = []
    

        for e in s:
            if e == "(":
                n.append('o')
                # print(n)
            else:
                if n and n[-1] == 'o':
                    n.pop()
                    n.append(1)
                    # print(n)
                elif n and n[-1] != 0:
                    n.append('c')
        
                
        
        sc = 0
        m = 1
        for e in n:
            if e == 'o':
                m *= 2
            elif e == 'c':
                m //= 2
            else:
                sc += (m * e)
            
                

        
        # print(n)
        # print(sc)
        return sc