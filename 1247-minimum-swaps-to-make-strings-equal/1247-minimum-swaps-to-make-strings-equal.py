class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        s1_count = Counter(s1)
        s2_count = Counter(s2)

        sum_x = s1_count["x"] + s2_count["x"]
        sum_y = s1_count["y"] + s2_count["y"]



        if sum_x % 2 == 1 or sum_y % 2 == 1:
            return -1
            


        steps = 0

        swaps = defaultdict(int)
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                swaps[(s1[i],s2[i])] += 1
        

        for swap in swaps:
            if swaps[swap] % 2 == 0:
                steps += (swaps[swap] // 2)
            else:
                steps += (swaps[swap] // 2) + 1
        return steps
            

        

