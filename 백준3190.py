# 백준 3190
# 뱀 25.02.10 14:25 start 16:24 end
'''
뱀을 구현해야함.
머리와 꼬리, 몸통이 있음. 
벽이나 자기자신의 몸에 머리가 충돌하면 끝

좌표들로 넣어놔야함
방향이 있음
머리 좌표가 몸통안에 있는 좌표에 다으면 끝, 벽에 다으면 끝
1부터 시작함!
뱀의 방향. 
몸마다 방향이 있어야함
자기 앞에 있는 값의 방향을 따라감
000
  0
  0 0
실수1: dir_move에서 값 하나 잘못돔
실수2: 문제이해, 머리가 움직인게 현재의 몸통에 부딫히면 fail! 미래의 몸뚱아리와 부딫힌다고 생각함..
틀림... 11%
사과를 먹는 경우도 머리를 돌릴 수 있는데 이 경우를 생각안했다..
'''
import collections
N = int(input())
K = int(input())
apple_pos = [tuple(map(int,input().split())) for _ in range(K)]
L = int(input())
snake_change_info = [tuple(input().split()) for _ in range(L)]

dir_move = [[0,1],[1,0],[0,-1],[-1,0]] # 오른쪽 , 아래, 왼쪽, 위쪽 
# 시계회전: snake_dir + 1 if snake_dir < 3 else 0
# 반시계회전: snake_dir - 1 if snake_dir > 0 else 3

def turn_clock(snake_dir):
    snake_dir = snake_dir + 1 if snake_dir < 3 else 0
    return snake_dir
def turn_anit_clock(snake_dir):
    snake_dir = snake_dir - 1 if snake_dir > 0 else 3
    return snake_dir

snake_body = collections.deque()
snake_body.appendleft((1,1,0)) # r,c,dir
time_info = collections.deque(snake_change_info)

def end_condition(next_pos,body_pos=(0,0)):
    if next_pos[0] <=0 or next_pos[1] <=0 or next_pos[0] >N or next_pos[1] > N:
        return True
    if next_pos == body_pos:
        return True
    return False
time = 0
end = False

while True:
    
    head_r,head_c,next_dir = snake_body.popleft() # 머리
    next_head_r , next_head_c = head_r+dir_move[next_dir][0],head_c+dir_move[next_dir][1]
    next_pos = (next_head_r , next_head_c)
    
    #print("t:",time,"h:", (next_head_r , next_head_c,next_dir))
    #print("now_snake:",snake_body)
    
    time += 1 # 8초가 끝낼때여야 하는데. 7초일때 방향을 바꾸고 있음 
    
    if end_condition(next_pos):
        break
    if next_pos in apple_pos:
        #print("eat!!")
        apple_pos.remove(next_pos) # 사과 먹음
        cur_dir = next_dir
        if time_info and time_info[0][0] == str(time):
            ti,turn = time_info.popleft()
            
            if turn == "D":
                next_dir = turn_clock(next_dir)
            if turn == "L":
                next_dir = turn_anit_clock(next_dir)
        snake_body.appendleft((head_r,head_c,cur_dir)) # 원래 머리를 몸으로
        snake_body.appendleft(((next_head_r , next_head_c,next_dir))) # 머리를 사과위치로
        
        #print("len snake:",len(snake_body))
        #print("now_snake:",snake_body)
        #print("========================")
        continue # 이동은 없음
    
    next_snake_body = collections.deque()
    next_snake_body.append((next_head_r,next_head_c,next_dir))
    
    while snake_body: # 몸 움직임
        r,c,dir = snake_body.popleft()
        next_r,next_c = r+dir_move[dir][0],c+dir_move[dir][1]
        
        if not end_condition(next_pos,(r,c)): # 현재의 몸통과 머리가 움직인게 부딫히는 건지 확인해야함!
            next_snake_body.append((next_r,next_c,next_dir))
            next_dir = dir 
        else:
            end = True
            break
        
    if end:
        break
    
    if time_info and time_info[0][0] == str(time):
        ti,turn = time_info.popleft()
        r,c,dir = next_snake_body.popleft()
        next_dir = dir 
        if turn == "D":
            next_dir = turn_clock(dir)
        if turn == "L":
            next_dir = turn_anit_clock(dir)
        next_snake_body.appendleft((r,c,next_dir))
    
    snake_body = next_snake_body
print(time)
        
        
        
    
    


