a=int(input("no.of rows in a matrix:"))
b=int(input(" no. of colunms in a matrix:"))
def mat_inv(a,b):
	if(a!=b):
		print"inverse of the matrix is not possible"
	else:
		out=[]
		r=[]
		c=[]
		for i in range(0,a):
			r += [0]
		for j in range(0,b):
			c += [0]
		for i in range(0,a):
			r[i] = c
		out=r
		print out
		for x in range(0,len(out)):
			for y in range(0,len(out[0])):
				out[x][y]=int(input(" elements for matrix:"))
		print out

mat_inv(a,b)
			
