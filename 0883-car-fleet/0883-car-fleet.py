class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        arr = list(zip(position,speed))
        arr.sort(key = lambda x:x[0], reverse = True)


        t = []
        for e in arr:
            p = e[0]
            s = e[1]

            tm = (target - p)/s
            t.append(tm)



        f = 1
        mn = t[0]
        for e in t:
            if e > mn:
                f += 1
                mn = e
            
        return f
             
