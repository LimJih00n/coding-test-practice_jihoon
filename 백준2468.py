# 백준 2468
# 안전영역. 25.02.03. 16:24 start
# 높이에 따라 잠기는 거 다름: N x N map이 주어지고 높이가 다 다름. 비 높이 이하인 부분은 모두 잠김 => 분할
# 최대로 분할 가능한 높이 구하기
# 높이: 최소값~최대값.
# 가장 간단
'''
모든 높이에 대해 영역 구하기 
영역구하기 => bfs or dfs

모든 영역에 대해 높이보다 높은지 & 방문한 것인지 확인. 방문안하면 bfs 진행 => 모두 방문할 수 있도로그, 아니면 cut

실수들: index 0과 1 실수, 움직인 거 봐여하는데 그냥 봄

# 틀렸습니다. 나옴 70% 쯤에서  - 17:06 => 조건 하나 고려안함. 모든 높이가 안잠길 수 있다
따라서 시작을 최소높이 -1에서 시작하게함 => clear
end: 25.02.03. 17:08
'''
from collections import deque 
dr = [1,-1,0,0]
dc = [0,0,1,-1]

N = int(input())
arr = [ list(map(int,input().split())) for i in range(N)]
max_h = float('-inf')
min_h = float('inf')
for cases in arr:
    for case in cases:
        max_h = max(case,max_h)
        min_h = min(case,min_h)

def check_b(node):
    if node[0]>=0 and node[1]>=0 and node[0]<N and node[1]<N:
        return True
    return False

def conut_safe(floored):
    
    count = 0
    
    visted = set()
    queue = deque()
    
    for r in range(N):
        for c in range(N):
            
            if arr[r][c] >floored and (r,c) not in visted:
                count += 1
                queue.append((r,c))
                visted.add((r,c))
                
                #print(r,c)
                while queue:
                    cur_node = queue.popleft()
                    for i in range(4):
                        next_r,next_c = cur_node[0] + dr[i],cur_node[1] + dc[i]
                        next_node = (next_r,next_c)
                        if check_b(next_node) and (next_node not in visted) and arr[next_r][next_c]>floored:
                            
                            queue.append(next_node)
                            visted.add(next_node)
    return count
ans = []
for h in range(min_h-1,max_h+1):
    ans.append(conut_safe(h))
print(max(ans))
    