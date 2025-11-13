class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        first transpose 
        the reverse each row

        """


            

        n = len(matrix)
        cm = [[0]*n for _ in range(n)]

        for i in range(n):
            for j in range(n):
                cm[j][i] = matrix[i][j]

        for r in range(n):
            i = 0
            j = n-1
            while i < j:
                cm[r][i], cm[r][j] = cm[r][j] , cm[r][i]
                i += 1
                j -= 1

        for i in range(n):
            for j in range(n):
                matrix[i][j] = cm[i][j]
        