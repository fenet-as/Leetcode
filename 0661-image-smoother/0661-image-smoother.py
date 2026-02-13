class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        
        def smoother(cell,mat):
            row = cell[0]
            col = cell[1]

            sum = 0
            count = 0

            for i in range(row-1,row+2):
                for j in range(col-1,col+2):
                    if 0 <= i < len(mat) and 0 <= j < len(mat[0]):
                        sum += mat[i][j]
                        count += 1

            return (sum//count)



        col = len(img[0])
        row = len(img)


        res = [[0]*col for _ in range(row)]

        for i in range(row):
            for j in range(col):
                res[i][j] = smoother((i,j),img)

        return res



