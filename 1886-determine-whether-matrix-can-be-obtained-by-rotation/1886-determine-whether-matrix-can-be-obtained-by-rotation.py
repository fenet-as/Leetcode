class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        

        def rotate(mat):
            rot = [[0]*len(mat) for _ in range(len(mat[0]))]

            for i in range(len(mat)):
                for j in range(len(mat[0])):
                    rot[j][i] = mat[i][j]

            for e in rot:
                i = 0
                j = len(e)-1
                while i < j:
                    e[i],e[j] = e[j],e[i]
                    i += 1
                    j -= 1
            return rot

        if mat == target:
            return True

        for _ in range(4):
            if rotate(mat) == target:
                return True
            mat = rotate(mat)
        
        return False