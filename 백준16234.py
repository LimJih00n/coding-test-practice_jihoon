#bfs 알고리즘 다시 복습
#인구이동
#문제 풀이 전 핵심 정리 24.12.19.15.45 시작 24.12.19.16.44 solve 
'''
국경선 공유 (4방향) 나라 인구차이 L이상 R이하면 국경선 열림
열린 칸들은 이동가능함
이동가능 한 수 // 그 마을 수 로 연합 인구 setting
다시 국경선 닫음

LR이하 없을때까지 반복

1. 입력 받았다 가정
2. 그냥 bfs로 탐색가능한 칸의 합 // 탐색한 칸 다 채움, => 반복하면서 마을 확인, 하루 지나고 다시 처음부터 확인하면서 마을 확인
3. bfs 진행 => 결과들 더 함
===========
연산 시간이 많이 걸리는데 solve?

계속 다 볼필요가 있는지 에대한 고찰 필요.

'''

from collections import deque
N,L,R = map(int,input().split())
arr = []
for i in range(N):
    arr.append(list(map(int,input().split())))

move_r = [1,-1,0,0]
move_c = [0,0,1,-1]
def check_b(r,c):
    if r>=0 and r < N and c>=0 and c<N:
        return True
    return False

def bfs(start_node,visted):
    
    queue = deque()
    
    visted.add(start_node)
    queue.append(start_node)
    our_con = set()
    our_con.add(start_node)
    
    sum_merge=0
    
    
    while queue:
        
        cur_node = queue.popleft()
        cur_r,cur_c = cur_node[0],cur_node[1]
        sum_merge += arr[cur_r][cur_c]
        
        for i in range(4):
            next_r,next_c = cur_r+move_r[i], cur_c+move_c[i]
            next_node = (next_r,next_c)
            
            if check_b(next_r,next_c) and next_node not in visted:
                abs_n = arr[cur_r][cur_c] -  arr[next_r][next_c] if arr[cur_r][cur_c] -  arr[next_r][next_c] > 0 else arr[next_r][next_c] -  arr[cur_r][cur_c]
                
                if L<= abs_n <=R:
                    queue.append(next_node)
                    visted.add(next_node)
                    our_con.add(next_node)
                
    return (len(our_con),sum_merge,our_con)
day_count = 0

def print_arr(arr):
    for i in range(len(arr)):
        print(arr[i])
    print("==========")
change=False
while True:
    visted = set()
    
    sum_merge = 0
    for r in range(N):
        for c in range(N):
            if (r,c) not in visted:
                
                (tot_len,sum_merge,our_con) = bfs((r,c),visted)
                
                if tot_len == 1:
                    continue
                
                for node in our_con:
                    arr[node[0]][node[1]] = sum_merge // tot_len
                change = True
    #print_arr(arr)
    if change==False:
        break
    change=False
    day_count +=1
    

print(day_count)
