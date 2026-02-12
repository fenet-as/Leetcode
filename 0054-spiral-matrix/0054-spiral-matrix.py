class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        

        def move(ll,rl,ul,dl,mat, fr,lc,lr,fc):
            res = []
            # left
            for j in range(ll,rl):
                res.append(mat[fr][j])


            # down
            for i in range(ul+1,dl):
                res.append(mat[i][lc])



            # right
            for j in range(rl-2,ll-1,-1):
                if fr == lr :
                    break
                res.append(mat[lr][j])

            # up

            for i in range(dl-2,ul,-1):
                if fc == lc :
                    break
                res.append(mat[i][fc])

            return res

        
        res = []

        ll = 0
        rl = len(matrix[0])

        ul = 0
        dl = len(matrix)

        fr = 0
        fc = 0
        lr = len(matrix) -1
        lc = len(matrix[0])-1

        while ll < rl and ul < dl:
            res.extend(move(ll,rl,ul,dl,matrix, fr,lc,lr,fc))
            ll += 1
            rl -= 1

            ul += 1
            dl -= 1

            fr += 1
            fc += 1
            lr -= 1
            lc -= 1
        return res



