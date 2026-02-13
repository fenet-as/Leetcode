def solution():

  
  mat = []
  for _ in range(5):
    row = list(map(int,input().split()))
    mat.append(row)

  for i in range(5):
    for j in range(5):
      if mat[i][j] == 1:
        return (abs((i+1)-3) + abs((j+1)-3))


print(solution())
