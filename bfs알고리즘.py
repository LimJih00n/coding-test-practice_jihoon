from collections import deque

visted = set()

def bfs(graph,start):
    
    queue = deque()
    queue.append(start)
    visted.add(start)
    
    while queue:
        
        v = queue.popleft()
        for n in graph[v]:
            if not n in visted:
                queue.append(n)
                visted.add(n)
# start node를 넣고, queue가 빌때까지 반복 -> front에서 빼내고 인접 노드 검사 -> 방문안했으면 반복, 방문처리. => 반복하기.
    
    