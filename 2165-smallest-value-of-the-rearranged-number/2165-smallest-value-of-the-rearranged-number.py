class Solution:
    def smallestNumber(self, num: int) -> int:
        
        if num == 0:
            return 0
        negative = False
        if num < 0:
            negative = True
            num = -1*num
        
        da = []

        while num:
            da.append(str(num%10))
            num = num//10
        
        if negative:
            da.sort(reverse = True)
            nn = int(''.join(da))
            return -1*nn

        else:
            da.sort()

            for i in range(len(da)):
                if da[i] != '0':
                    da[i],da[0] = da[0],da[i]
                    break
            nn = int(''.join(da))
            return nn
        



        
