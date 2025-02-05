#백준 5212
#구현문제
#25.02.05 14:40 start 25.02.05 15:05 end
'''
지구 온난화
X 에서 4방으로 몇개의 .이 닿아있나 확인. 
지도의 크기는 모든 섬을 포함하는 가장 작은 직사각형이다. 
50년이 지난 후에도 섬은 적어도 한 개 있다. 또, 지도에 없는 곳, 지도의 범위를 벗어나는 칸은 모두 바다이다.

1. X의 상하좌우로 . 확인 
2. 3이상일 경우 .으로 바꾸기. 미리 기록해둠
3. 남은 땅 출력하기 => 남은 땅 중 x좌표가 가장 작, y 좌표가 가장 큰. or y 좌표가 가장 작은 x좌표가 가장 큰
x좌표가 가장 작은
y좌표가 가장 작은
x좌표가 가장 큰
y좌표가 가장 큰
4점을 구해야함
set으로 지워지는 점들 관리하는 거 좋은 듯!
'''
R,C = map(int,input().split())
arr=[list(input()) for r in range(R)]
earth_set = [(r,c) for r in range(R) for c in range(C) if arr[r][c]=='X']
tot_set =[]
min_x = float('inf')
min_y = float('inf')
max_x = float('-inf')
max_y = float('-inf')

change_set = []
dr = [1,-1,0,0]
dc = [0,0,1,-1]
for earth in earth_set:
    count = 0
    
    for i in range(4):
        next_r,next_c = earth[0]+dr[i] , earth[1]+dc[i]
        if next_r>=R or next_c>=C or next_c<0 or next_r<0:
            count +=1
        if next_r<R and next_c<C and next_c>=0 and next_r>=0 and arr[next_r][next_c] =='.':
            count +=1
    if count==3 or count==4:
        change_set.append((earth[0],earth[1]))

tot_set = list((set(earth_set) - set(change_set)))

for p in tot_set:
    
    max_x = max(p[0],max_x)    
    max_y = max(p[1],max_y)    
    min_x = min(p[0],min_x)    
    min_y = min(p[1],min_y)    
        
        
for case in change_set:
    arr[case[0]][case[1]] = '.'

#print as
for r in range(min_x,max_x+1):
    for c in range(min_y,max_y+1):
        print(arr[r][c],end="")
    print()
        