import copy
def is_safeX(x,n):
	return (x>=0 and x<n)

def is_safeY(y,m):
	return(y>=0 and y<m)

def bomb_matrix(x,y,m):
	saveval=m[x][y]
	for i in range(-1,2):
		for j in range(-1,2):
			curX=x+i
			curY=y+j
			if is_safeX(curX,len(m[0])) and is_safeY(curY,len(m)):
				m[x][y]=saveval
				value=m[curX][curY]-m[x][y]
				if  value<0:
					value=0
				m[curX][curY]=value
	m[x][y]=saveval
	return m
def sum_elements_in_matrix(m):
	sums=0
	for i in range(len(m[0])):
		for j in range(len(m)):
			sums+=m[i][j]
	return sums

def matrix_bombing_plan(m):
	dict={}
	for i in range(len(m[0])):
		for j in range(len(m)):
			temp=copy.deepcopy(m)
			temp=bomb_matrix(i,j,temp)
			sums=sum_elements_in_matrix(temp)
			dict[(i,j)]=sums

	return dict

print(matrix_bombing_plan([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))


