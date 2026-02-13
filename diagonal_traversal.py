class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        
        def valid_move(mat,curr,dir):
            row = curr[0]
            col = curr[1]

            # dir - 1 = up right
            # dir - 0 = left down

            res = []
            res.append(mat[row][col])
            while True:
                if dir == 1:
                    next_r = row - 1
                    next_c = col + 1

                    if 0 <= next_r <len(mat) and 0 <= next_c <len(mat[0]):
                        res.append(mat[next_r][next_c])
                    else:
                        break
                
                if dir == 0:
                    next_r = row + 1
                    next_c = col - 1

                    if 0 <= next_r <len(mat) and 0 <= next_c <len(mat[0]):
                        res.append(mat[next_r][next_c])
                    else:
                        break
                row = next_r
                col = next_c

            return [res,(row,col)]

        r = len(mat)
        c = len(mat[0])


        curr_r = 0
        curr_c = 0
        res = []
        dir = 1

        while 0 <= curr_r < r and 0 <= curr_c < c:

            move = valid_move(mat,(curr_r,curr_c),dir)
            res.extend(move[0])

            curr = move[1]

            if dir == 1:
                if curr[1]  == (c-1):
                    curr_r = curr[0] + 1
                    curr_c = curr[1] 
                else:
                    curr_c = curr[1] + 1
                    curr_r = curr[0]
                
                dir = 0
            
            else:
                if curr[1]  == 0 and (curr[0] + 1) < r:
                    curr_r = curr[0] + 1
                    curr_c = curr[1] 
                else:
                    curr_c = curr[1] + 1
                    curr_r = curr[0]
                
                dir = 1     

        return res         



                    
            
                        




