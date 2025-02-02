# 토마토
# 익은 토마토는 상하좌우위아래를 다시 익힘
# 다익게 되는 경우 구하기 => 최소일수
from collections import deque

M,N,H = map(int,input().split())
arr = []

move_n = [1,-1,0,0,0,0]
move_m = [0,0,1,-1,0,0]
move_h = [0,0,0,0,1,-1]


for h in range(H):
    box = []
    for n in range(N):
        box.append(list(map(int,input().split())))
    arr.append(box)

to_init_set = [(h,n,m) for h in range(H) for n in range(N) for m in range(M) if arr[h][n][m] == 1]
tot_unto = sum([1 for h in range(H) for n in range(N) for m in range(M) if arr[h][n][m] == 0])


def check_B(h,n,m):
    if h<H and n<N and m<M and h>=0 and n>=0 and m>=0:
        return True
    return False

def bfs():
    global tot_unto
    visted = set()
    queue = deque()
    for node in to_init_set:
        visted.add(node)
        queue.append(node)
        arr[node[0]][node[1]][node[2]] = 0
    min_time = 0
        
    while queue:
        cur_node = queue.popleft()
        
        for i in range(6):
            
            next_node = (cur_node[0] + move_h[i] ,cur_node[1] + move_n[i] ,cur_node[2] + move_m[i])
            if check_B(next_node[0],next_node[1],next_node[2]) and arr[next_node[0]][next_node[1]][next_node[2]] != -1 and next_node not in visted:
                visted.add(next_node)
                queue.append(next_node)
                arr[next_node[0]][next_node[1]][next_node[2]] = arr[cur_node[0]][cur_node[1]][cur_node[2]] + 1
                tot_unto -= 1
                if min_time < arr[next_node[0]][next_node[1]][next_node[2]]:
                    min_time = arr[next_node[0]][next_node[1]][next_node[2]]
    if tot_unto !=0:
        return -1
    else:
        return min_time

#h, n,m


if tot_unto == 0:
    print(0)
else:
    print(bfs())
    
        

    
