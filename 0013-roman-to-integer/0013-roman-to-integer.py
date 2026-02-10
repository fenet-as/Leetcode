class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0

        value = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000

        }
        i = 0
        while i < (len(s)-1):
            if s[i:i+2] == "IV":
                num += 4
            elif s[i:i+2] == "IX":
                num += 9
            elif s[i:i+2] == "XL":
                num += 40
            elif s[i:i+2] == "XC":
                num += 90
            elif s[i:i+2] == "CD":
                num += 400
            elif s[i:i+2] == "CM":
                num += 900
            else:
                num += value[s[i]]
                i += 1
                continue
            i += 2
        
        if i < len(s):
            num += value[s[i]]
                
        return num

