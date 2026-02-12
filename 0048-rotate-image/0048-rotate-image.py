class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        def rev(arr):
            i = 0
            j = len(arr)-1

            while i < j:
                arr[i],arr[j] = arr[j],arr[i]
                i += 1
                j -= 1
    


        i = 0
        j = 0
        while i < len(matrix) and j  < len(matrix[0]):
            for r in range(i, len(matrix[0])):
                matrix[r][j],matrix[j][r] = matrix[j][r],matrix[r][j]
            i += 1
            j += 1

        for r in matrix:
            rev(r)


        

