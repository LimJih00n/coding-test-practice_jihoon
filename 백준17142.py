#연구소 3
# => bfs로 풀어야함, dfs로 접근할 경우 순차적 탐색이 안됨 => 탐색의 경우 가능하면 bfs
#모두 보는 경우 이나 각 노드들이 얼마나 뻗어가는가를 보는 것임
from collections import deque
import copy

move_r = [1,-1,0,0]
move_c = [0,0,-1,1]

N,B = map(int,input().split())
arr = []
for i in range(N):
    arr.append(list(map(int,input().split())))

bi_init_po = [(r,c) for r in range(N) for c in range(N) if arr[r][c]==2]
bi_able_po_set = []

def gen_c(elements,r):
    re = []
    def dfs(start, path):
        if len(path) == r:
            re.append(path[:])
            return
        for i in range(start,len(elements)):
            path.append(elements[i])
            dfs(i+1,path)
            path.pop()
    dfs(0,[])
    return re
bi_able_po_set = gen_c(bi_init_po,B)

def check_B(r,c):
    if r<N and c<N and r>=0 and c>=0:
        return True
    return False

def print_map(arr_si):
    print("==========")
    for i in range(N):
        print(arr_si[i])
    print("==========")

def make_init_map(po_set):
    arr_si = copy.deepcopy(arr)
    for i in range(B):
        arr_si[po_set[i][0]][po_set[i][1]] = 0
    
    safe_arr = 0
    
    for r in range(N):
        for c in range(N):
            if arr_si[r][c]==1:
                arr_si[r][c]= "-"
            elif arr_si[r][c]==2:
                arr_si[r][c]= "*"
            elif (r,c)not in po_set and arr_si[r][c] == 0:
                safe_arr +=1
    return (arr_si,safe_arr)

def bi_simul(g,safe_arr,nodes):
    visted = set()
    queue = deque()
    for node in nodes:
        visted.add(node)
        
        queue.append(node)
    
    min_bi_time = 0
    
    while queue:
        
        v = queue.popleft()
        cur_r,cur_c  = v[0],v[1]
  
            
        #print_map(g)
        
        
        for i in range(4):
            next_r = v[0] + move_r[i]
            next_c = v[1] + move_c[i]
            next_node = (next_r,next_c)
            
            if check_B(next_r,next_c) and g[next_r][next_c] == "*" and next_node not in visted:
                queue.append(next_node)
                g[next_r][next_c] = g[cur_r][cur_c] + 1
                visted.add(next_node)
            
            elif check_B(next_r,next_c) and g[next_r][next_c] != "-" and next_node not in visted:
                g[next_r][next_c] = g[cur_r][cur_c] + 1
                queue.append(next_node)
                visted.add(next_node)
                safe_arr -= 1
                if type(g[next_r][next_c])==int and g[next_r][next_c] > min_bi_time:
                    min_bi_time = g[next_r][next_c]
                    
    #print(nodes,min_bi_time,safe_arr)
    #print_map(g)
    
    if safe_arr == 0:
        return min_bi_time
    else:
        return -1
ans = []
#print(bi_able_po_set)

for po_set in bi_able_po_set:
    arr_si,safe_arr = make_init_map(po_set)
    an = bi_simul(arr_si,safe_arr,po_set)
    if an >= 0 :
        ans.append(an)
if len(ans):
    print(min(ans))
else:
    print(-1)
            


# 바이러스를 놓을 수 있는 모든 위치 구하기 # 조합 B개
# 바이러스를 놓고 퍼져나가는 시간 구하기 => 놓고 퍼져나가기 simul 그리고 시간 구하기. 
# 최소값 비교하기
# 모두 못채우는 경우는 -1임 => 0 겨
# 표시를 어떻게 할까??
# 마지막이 *인 경우에는 최소 시간에 표시할 필요가 없음이 핵심!

# 헤맨 부분: 