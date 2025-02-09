#백준 1743
# 25.02.09 21:20 start 25.02.09. 21:28 end
'''
음식물 쓰레기 크기 구하기.
좌표들중 연결된거 확인해서 크기 구하면 됨
좌표로 주어짐
이동크기 제는게 하나
'''
import collections as col 
N,M,K = map(int,input().split())
arr = [tuple(map(int,input().split())) for _ in range(K)]
dr = [1,-1,0,0]
dc = [0,0,1,-1]
visited = set()
def bfs(start):
    global visited
    queue = col.deque()
    visited.add(start)
    queue.appendleft(start)
    size = 1
    
    while queue:
        cur_node = queue.popleft()
        for i in range(4):
            next_r,next_c = cur_node[0]+dr[i],cur_node[1]+dc[i]
            
            if next_c >0 and next_c<=M and next_r<=N and next_r>0 and (next_r,next_c) not in visited and (next_r,next_c) in arr:
                visited.add((next_r,next_c))
                size += 1
                queue.append((next_r,next_c))
    return size
max_ = 0
for node in arr:
    if node not in visited:
        max_ = max(max_,bfs(node))
print(max_)



