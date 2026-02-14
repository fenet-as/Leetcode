class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        


        for e in image:
            i = 0
            j = len(image)-1

            while i <= j:
                e[i],e[j]=e[j],e[i]

                i += 1
                j -= 1

        for e in image:
            for i in range(len(e)):
                e[i] = 0 if e[i] == 1 else 1

        
            
        return image