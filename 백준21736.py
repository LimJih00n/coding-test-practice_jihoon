#백준 21736 25.02.19 21:46 start
'''
bfs 단순 탐색 문제

'''
import collections

def bfs(start):
    visted = set()
    visted.add(start)
    queue = collections.deque()
    queue.append(start)
    meet_per = 0
    while queue:
        cur_node = queue.popleft()
        for i in range(4):
            next_r,next_c = cur_node[0]+dr[i],cur_node[1] + dc[i]
            next_node = (next_r,next_c)
            if next_r>=0 and next_c>=0 and next_c<M and next_r<N and next_node not in visted:
                if arr[next_r][next_c] !='X':
                    if arr[next_r][next_c] == 'P':
                        meet_per +=1
                    queue.append(next_node)
                    visted.add(next_node)
    return meet_per if meet_per != 0 else "TT"

N,M = map(int,input().split())
arr = [list(input()) for _ in range(N)]
start_po = [(r,c) for r in range(N) for c in range(M) if arr[r][c]=='I']

dr = [1,-1,0,0]
dc = [0,0,1,-1]
print(bfs(start_po[0]))

