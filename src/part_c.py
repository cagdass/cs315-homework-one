import numpy as np

# Position class to hold the coordinates of a vertex
class Position:
	def __init__(self, x, y):
		self.x = x
		self.y = y

# a function that checks if all the adjacent elements to a vertex are zero
def adjEmpty(position, s, size):
	mat = np.matrix(s)
	X = position.x
	Y = position.y
	i = 0

	# i is incremented each time an adjacent point has value zero
	if( X - 1 >= 0 and Y - 1 >= 0):
		if( mat[X-1, Y-1] == 0):
			i += 1
	if( X - 1 >= 0):
		if( mat[X-1, Y] == 0):
			i += 1
	if( X -1 >= 0 and Y + 1 < size):
		if( mat[X-1, Y+1] == 0):
			i += 1
	if( Y - 1 >= 0):
		if( mat[X, Y-1] == 0):
			i += 1
	if( Y + 1 < size):
		if( mat[X, Y+1] == 0):
			i += 1
	if( X + 1 < size and Y - 1 >= 0):
		if( mat[X+1, Y-1] == 0):
			i += 1
	if( X + 1 < size):
		if( mat[X+1, Y] == 0):
			i += 1
	if( X + 1 < size and Y + 1 < size):
		if( mat[X+1, Y+1] == 0):
			i += 1
	
	# i == 8 means all the numbers are zero so it will tell function find to stop executing as there is nowhere left to go
	return i == 8

# number of paths found, yeah global :) :(
paths = 0

def find(s, size, position, target, count, length):
	global paths
	
	# a brand new matrix, for a recursive call with the previously visited vertices are set to zero
	curMatrix = np.matrix(s)
	
	curX = position.x
	curY = position.y
	tarX = target.x
	tarY = target.y

	if( curX == tarX and curY == tarY and count == length):
		paths += 1
	else:
		# termination
		if( adjEmpty(position, s, size)):
			return None
		else:
			# a new string is created and current point is set to zero before moving on to next nonzero point so that 
			# there is no coming back and getting stuck back and forth on already-visited vertex
			st = s[0:curX*size*2 + curY*2] + '0' + s[curX*size*2 + curY*2 + 1: len(s)]

			# does not look any bright at all, it checks whether the adjacent vertex is within the bounds
			# and then it checks if it is not zero so there is a point in such venture
			if(curX + 1 < size and curY + 1 < size):
				if(curMatrix[curX + 1, curY + 1] != 0):
					find(st, size, Position(curX + 1, curY + 1), target, count + 1, length)
			if(curX + 1 < size):
				if(curMatrix[curX + 1, curY] != 0):
					find(st, size, Position(curX + 1, curY), target, count + 1, length)
			if(curX + 1 < size and curY - 1 >= 0):
				if(curMatrix[curX + 1, curY - 1] != 0):
					find(st, size, Position(curX + 1, curY - 1), target, count + 1, length)
			if(curY + 1 < size):
				if(curMatrix[curX, curY + 1] != 0):
					find(st, size, Position(curX, curY + 1), target, count + 1, length)
			if(curY - 1 >= 0):
				if(curMatrix[curX, curY - 1] != 0):
					find(st, size, Position(curX, curY - 1), target, count + 1, length)
			if(curX - 1 >= 0 and curY + 1 < size):
				if(curMatrix[curX - 1, curY + 1] != 0):
					find(st, size, Position(curX - 1, curY + 1), target, count + 1, length)
			if(curX - 1 >= 0):
				if(curMatrix[curX - 1, curY] != 0):
					find(st, size, Position(curX - 1, curY), target, count + 1, length)
			if(curX - 1 >= 0 and curY - 1 >= 0):
				if(curMatrix[curX - 1, curY - 1] != 0):
					find(st, size, Position(curX - 1, curY - 1), target, count + 1, length)	

# positions of the nonzero values are stored in this list
pos = []

# imagining a directory not without a file called input.txt
file = open('input.txt', 'read')
file.readline() # eat [num_nodes]
size = int(file.readline()) # get matrix size
file.readline() # eat \n
file.readline() # eat [edges]

for line in file:
	dash = line.index(' -- ')
	# each number that comes right before and after [ -- ] are made into Position objects and stored in the list
	pos.append(Position(int(line[0:dash]), int(line[dash+4:len(line)])))
	if( int(line[0:dash]) != int(line[dash+4:len(line)])):
		pos.append(Position(int(line[dash+4:len(line)]), int(line[0:dash])))

matrixstr = ''

# I don't know any better than this on initializing a NumPy matrix without a string
for r in range(0, size):
	for c in range(0, size):
		if(c < size - 1):
			matrixstr += '0 '
		else:
			matrixstr += '0'
	if (r < size - 1):
		matrixstr += ';'

for item in pos:
	matrixstr = matrixstr[0:item.x*size*2 + item.y*2] + '1' + matrixstr[item.x*size*2 + item.y*2 + 1: len(matrixstr)]

# print np.matrix(matrixstr)

# how many times the current vertex changes in the traverser function
pointChange = 0

# number of vertices to be visited
length = 3

# coordinates of the given vertex
initialX = 1
initialY = 2

# coordinates of the target vertex
targetX = 3
targetY = 3

# function execution
find(matrixstr, size, Position(initialX, initialY), Position(targetX, targetY), pointChange, length)

print 'Number of paths from [' + str(initialX) + ', ' + str(initialY) + '] to [' + str(targetX) + ', ' + str(targetY) + '] is ' + str(paths)

