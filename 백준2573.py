# 백준 2573
# bfs연습 중
# 25.02.03 17:16 start 25.18.40 end. 
# => 오타 찾는 데 시간이 좀 걸림
'''
문제 0과 나머지 수, 0으로 붙어 있는 영역만큼 값 뺌
영역을 세야함. 2개 이상으로 분리되는 순간. 의 해 구하기. 만약 분리 안되고 다 녹는 경우 0

0이상의 값이 0과 인접한지 확인하고 값빼기
분리된건지 확인하기. => 연결된 모든 노드 확인했는데 0이상의 값이 남아있는 경우.     

solve one. ice count를 둠. 모두 녹은 경우가 아니라면. 즉 max에서 count했는데 모두 방문하는 경우는 pass 아닌 경우에는 끝
다 녹는 경우도 따로 처리함

문제1: 녹이고 나서 max ice를 찾아야함.

문제2: 18:04 제출 -> 틀림 => 처음 부터 2덩이는 0년으로
오타: if next_r<N and next_c<M and next_r>=0 and next_c>=0 and (next_r,next_c) not in visted and arr[next_r][next_c] >0:
조건식 부분에서 잘못씀. 그냥 함수 만들어서 조금 느리더라도 처리하는 게 맞는 듯!
'''
from collections import deque

dr = [1,-1,0,0]
dc = [0,0,1,-1]

N,M = map(int,input().split())
arr = [list(map(int,input().split())) for i in range(N)]



def one_year(year):
    global arr
    max_ = 0
    max_ice=(0,0)
    ice_set = []
    non_ice_count = 0
    for r in range(N):
        for c in range(M):
            if arr[r][c] <=0:
                continue
            
            ice = 0
            non_ice_count += 1
            for i in range(4):
                if r+dr[i]>=0 and c+dc[i]>= 0 and r+dr[i]<N and c+dc[i]<M and arr[r+dr[i]][c+dc[i]]==0:
                    ice += 1
         #   print(r,c,ice)
            
            if max_ < arr[r][c]-ice and arr[r][c]-ice>0:
                max_ = arr[r][c] 
                max_ice = (r,c)
            ice_set.append((r,c,ice))
    if year != 0:    
        for case in ice_set:
            if arr[case[0]][case[1]] - case[2] >0:
                arr[case[0]][case[1]] -= case[2]
            else:
                arr[case[0]][case[1]] = 0
                non_ice_count -=1
    #print("m",max_)
    if max_ == 0:
        return -1
    visted = set()
    visted.add(max_ice)
    queue=deque()
    queue.append(max_ice)
    count_area = 1
    
    while queue: #max ice로 부터 시작해 영역을 셈. 
        cur_node = queue.popleft()
        
        for i in range(4):
            next_r ,next_c = cur_node[0]+dr[i], cur_node[1]+dc[i]
            
            if next_r<N and next_c<M and next_r>=0 and next_c>=0 and (next_r,next_c) not in visted and arr[next_r][next_c] >0:
            
                visted.add((next_r,next_c))
                queue.append((next_r,next_c))
            
                count_area +=1
    #for r in arr:
     #   print(r)
    #print(non_ice_count,count_area)
    if non_ice_count == count_area:
        return 1
    if year == 0:
        return 3
    return 0

year = 0

if one_year(year) == 3:
       print(0)
else:
    while True:
        year +=1
        re = one_year(year)
        if re==1:
            continue
        elif re==-1:
            print(0)
            break
        else:
            print(year)
            break
    
    