#백준2251
#25.02.04 14:45 start 25.02.04 16:04 end
'''
다차거나 0이될때까지 
A B C 있고 C에는 모두 차있음 
첫 번째 물통(용량이 A인)이 비어 있을 때, 세 번째 물통(용량이 C인)에 담겨있을 수 있는 물의 양을 모두 구해내는 프로그램을 작성하시오.
C -> B or C->A
감이 전혀 안옴..
본래 상태로 돌아오면 종료. 
상태: [(양,부피),(양,부피),(양,부피)]
now에 따라 옮김 다름
경우는 항상 2가지. 있었던 상태면 끝 내기. 초기 상태면 끝내기.
state만 있고 now는 별로 중요하지 않음.
그냥
A->B
A->C
B->A
B->C
C->A
C->B
모두 필요함.

처음에 문제 이해한 데 시간이 꽤 걸렸다.
핵심은 모든 경우를 다보는 것. 있었던 상태이면 끝내는 것.
'''


A,B,C = map(int,input().split())
init_state = ((0,A),(0,B),(C,C)) #0:A 1:B 2:C
visited_state = set()
dic_ ={
    0:"A",1:"B",2:"C"
}
ans = set()
def dfs(now,now_state):
    if now_state in visited_state:

        return
    visited_state.add(now_state)
    A_cap = now_state[0][0]
    B_cap = now_state[1][0]
    C_cap = now_state[2][0]
    
    
    #A->B
    if  A_cap + now_state[1][0] >= now_state[1][1]: # 모두 차는 경우
        next_cap = now_state[1][1]
        rest_cap = A_cap- (now_state[1][1] - now_state[1][0])
        next_state = ((rest_cap,A),(next_cap,B),(C_cap,C))
        dfs(1,next_state)
    else: # 다 
        next_cap = A_cap + now_state[1][0]
        rest_cap = 0
        next_state = ((rest_cap,A),(next_cap,B),(C_cap,C))
        dfs(1,next_state)
    #A->C
    if  A_cap + now_state[2][0] >= now_state[2][1]: # 모두 차는 경우
        next_cap = now_state[2][1]
        rest_cap = A_cap - (now_state[2][1] - now_state[2][0])
        next_state = ((rest_cap,A),(B_cap,B),(next_cap,C))
        dfs(2,next_state)
    else: # 다
        next_cap = A_cap + now_state[2][0]
        rest_cap = 0
        next_state = ((rest_cap,A),(B_cap,B),(next_cap,C))
        dfs(2,next_state)
    ####
    #B->A
    if  B_cap + now_state[0][0] >= now_state[0][1]: # 모두 차는 경우
        next_cap = now_state[0][1]
        rest_cap =B_cap - (now_state[0][1] - now_state[0][0])
        next_state = ((next_cap,A),(rest_cap,B),(C_cap,C))
        dfs(0,next_state)
    else: # 다
        next_cap = B_cap + now_state[0][0]
        rest_cap = 0
        next_state = ((next_cap,A),(rest_cap,B),(C_cap,C))
        dfs(0,next_state)
    #B->C
    if  B_cap + now_state[2][0] >= now_state[2][1]: # 모두 차는 경우
        next_cap = now_state[2][1]
        rest_cap = B_cap - (now_state[2][1] - now_state[2][0])
        next_state = ((A_cap,A),(rest_cap,B),(next_cap,C))
        dfs(2,next_state)
    else: # 다
        next_cap = B_cap + now_state[2][0]
        rest_cap = 0
        next_state = ((A_cap,A),(rest_cap,B),(next_cap,C))
        dfs(2,next_state)
    ####
    #C
    #C->A
    if  C_cap + now_state[0][0] >= now_state[0][1]: # 모두 차는 경우
            next_cap = now_state[0][1]
            rest_cap = C_cap - (now_state[0][1] - now_state[0][0])
            next_state = ((next_cap,A),(B_cap,B),(rest_cap,C))
            dfs(0,next_state)
    else: # 다
        next_cap = C_cap + now_state[0][0]
        rest_cap = 0
        next_state = ((next_cap,A),(B_cap,B),(rest_cap,C))
        dfs(0,next_state)
    #C->B
    if  C_cap + now_state[1][0] >= now_state[1][1]: # 모두 차는 경우
        next_cap = now_state[1][1]
        rest_cap = C_cap - (now_state[1][1] - now_state[1][0])
        next_state = ((A_cap,A),(next_cap,B),(rest_cap,C))
        dfs(1,next_state)
    else: # 다 
        next_cap = C_cap + now_state[1][0]
        rest_cap = 0
        next_state = ((A_cap,A),(next_cap,B),(rest_cap,C))
        dfs(1,next_state)

    
    #print("now:",dic_[now],now_state)
    if now_state[0][0] == 0:
     #   print(now_state[2][0])
        ans.add(now_state[2][0])


dfs(2,init_state)
print(*sorted(ans))
