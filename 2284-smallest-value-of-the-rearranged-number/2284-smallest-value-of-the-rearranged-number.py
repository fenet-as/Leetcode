class Solution:
    def smallestNumber(self, num: int) -> int:
        '''

        unpack all the elemnts and add them to array
        consider thier signs


        sort them in increasing if +ve 
        and decreasing if -ve

        if +ve:
            check that the first element is  not zero

            if it is zero:
                for i in range(1,len(na)):
                    if na[i] != 0:
                        na[i],na[0]=na[0],na[i]\
                        break
        for e in na:
            e = str(e)
        rn = ''.join(na)
        rn = int(rn)

        finally return it's sign 
        if ip:
            return rn
        return -1*rn

            




        na = []

        ip = True
        if num < 0:
            ip = False
            num *= -1
        

        for e in str(num):
            na.append(int(e))
        
        if ip:
            na.sort()
            if na[0] == 0:
                for i in range(1,len(na)):
                    if na[i] != 0:
                        na[i],na[0]=na[0],na[i]
                        break
        else:
            na.sort(reverse = True)

        for e in na:
            e = str(e)
        rn = ''.join(na)
        rn = int(rn)


        if ip:
            return rn
        return -1*rn


        
        

        '''

        na = []

        ip = True
        if num < 0:
            ip = False
            num *= -1
        

        for e in str(num):
            na.append(int(e))
        
        if ip:
            na.sort()
            if na[0] == 0:
                for i in range(1,len(na)):
                    if na[i] != 0:
                        na[i],na[0]=na[0],na[i]
                        break
        else:
            na.sort(reverse = True)
        

        for i in range(len(na)):
            na[i] = str(na[i])

        
        
        rn = ''.join(na)
        rn = int(rn)


        if ip:
            return rn
        return -1*rn
