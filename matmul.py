x=[[1,2,3],
    [4,5,6],
    [7,8,9]]
y=[[2,2,2],
    [3,3,3],
    [4,4,4]]
output=[[0,0,0],
            [0,0,0],
            [0,0,0,]]
for i in range(len(x)):
  for j in range(len(y[0])):
    for k in range(len(y)):
      output[i][j]+=x[i][k]*y[k][j]
for o in output:
  print(o)