i_count = 0 

graph = [
    [1, 0, 1, 0],
    [0, 0, 0, 0],
    [1, 1, 1, 0],
    [0, 0, 0, 1]
]

move_4 = [(1,0),(-1,0),(0,1),(0,-1)] # (r,c) => 
R = len(graph)
C = len(graph[0])
visited = set()

def dfs(node):
    global graph
    if node not in visited and graph[node[0]][node[1]]:
        print(f"{node}방문")
        graph[node[0]][node[1]] = 0
        for i in range(4):
            next_node = (node[0]+move_4[i][0],node[1]+move_4[i][1])
            if next_node[0] < R and next_node[0]>=0 and next_node[1]<C and next_node[1]>=0:
                print("이동")
                dfs(next_node)
    

for r in range(len(graph)): #0,1,2
    for c in range(len(graph[r])):
        if graph[r][c]:
            print((r,c),"는 1")
            dfs((r,c))
            i_count +=1

print(i_count)