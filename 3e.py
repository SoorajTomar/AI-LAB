#Graph Coloring Using R Consistency
def graphColoring(graph,color):
    color[0]=[1,0]
    for i in range(4):
        print("In node :",i)
        for j in range(4):
            if(graph[i][j]!=0):
                for k in range(2):
                    if color[i][k]!=0 and color[j][k]==color[i][k]:
                        color[j][k]=0
    print(color)
if __name__ == '__main__':
    graph = [[0, 1, 1, 0],[1, 0, 0, 1],[1, 0, 0, 1],[0, 1, 1, 0]]
    color = [[1,2] for i in range(4)]
    graphColoring(graph,color)
