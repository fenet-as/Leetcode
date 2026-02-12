class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """


        r = len(matrix)
        c = len(matrix[0])

        fr = False

        for j in range(c):
            if matrix[0][j] == 0:
                fr = True

        fc = False

        for i in range(r):
            if matrix[i][0] == 0:
                fc = True


        
        

        for i in range(1,r):
            for j in range(1,c):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0


        for i in range(1,r):
            for j in range(1,c):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        if fc == True:
            for i in range(r):
                matrix[i][0] = 0
        if fr == True:
            for j in range(c):
                matrix[0][j] = 0




        

