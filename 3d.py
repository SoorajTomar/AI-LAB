#Graph Coloring Using Backtracking
def isSafe(graph, color):
	for i in range(5):
		for j in range(i + 1, 5):
			if (graph[i][j] and color[j] == color[i]):
				return False
	return True
def graphColoring(graph, m, i, color):
	if (i == 5):
		if (isSafe(graph, color)):
			printSolution(color)
			return True
		return False
	for j in range(1, m + 1):
		color[i] = j
		if (graphColoring(graph, m, i + 1, color)):
			return True
		color[i] = 0
	return False
def printSolution(color):
	print("Solution Exists:" " Following are the assigned colors ")
	for i in range(5):
		print(color[i], end=" ")
if __name__ == '__main__':
	graph = [
		[0, 1, 1, 0, 0],
		[1, 0, 1, 0, 1],
		[1, 1, 0, 0, 1],
		[0, 0, 0, 0, 1],
        [0, 1, 1, 1, 0]
	]
	m = 3
	color = [0 for i in range(5)]
	if (not graphColoring(graph, m, 0, color)):
		print("Solution does not exist")
