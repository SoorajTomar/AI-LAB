#Best First Search
from queue import PriorityQueue
v = 14
graph = [[] for i in range(v)]
def best_first_search(actual_Src, target, n):
	visited = [False] * n
	pq = PriorityQueue()
	pq.put((0, actual_Src))
	visited[actual_Src] = True
	while pq.empty() == False:
		u = pq.get()[1]
		print(u, end=" ")
		if u == target:
			break
		for v, c in graph[u]:
			if visited[v] == False:
				visited[v] = True
				pq.put((c, v))
	print()
def add(x, y, cost):
	graph[x].append((y, cost))
	graph[y].append((x, cost))
add(0, 1, 3)
add(0, 2, 6)
add(0, 3, 5)
add(1, 4, 9)
add(1, 5, 8)
add(2, 6, 12)
add(2, 7, 14)
add(3, 8, 7)
add(8, 9, 5)
add(8, 10, 6)
add(9, 11, 1)
add(9, 12, 10)
add(9, 13, 2)
source = 0
target = 7
best_first_search(source, target, v)
