class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        '''
        j = c//2
        i = 1

        1 4
        17
        1 3

        0 1
        1 1

        1  2

        '''
        if c == 0 or c == 1:
            return True

        

        i = 0
        j = int(math.sqrt(c))

        while i <= j :
            pdt = j*j + i*i
            if pdt == c:
                return True
            elif pdt > c:
                j -= 1
            else:
                i += 1

        return False
