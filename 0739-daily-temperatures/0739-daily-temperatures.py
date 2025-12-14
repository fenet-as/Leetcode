class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        '''
        st =[]

        na = []
        for i in range(len(temp)):
            na.append((temp[i],i))

        for i in range(len(na)-1,-1,-1):
            ea = na[i]
            e = ea[0]
            

            while st and st[-1][0] < e:
                st.pop()

            if st:
                ind = st[-1][1]
                res[i] = ind - ea[1]
            else:
                res[i] = 0

            st.append(ea)
        return res
        '''
        st =[]
        res = [0]*len(temp)

        na = []
        for i in range(len(temp)):
            na.append((temp[i],i))

        for i in range(len(na)-1,-1,-1):
            ea = na[i]
            e = ea[0]
            

            while st and st[-1][0] <= e:
                st.pop()

            if st:
                ind = st[-1][1]
                res[i] = ind - ea[1]

            else:
                res[i] = 0
            

                
            st.append(ea)
        return res