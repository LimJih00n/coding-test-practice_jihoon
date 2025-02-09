#백준 16987
# 계란으로 계란치기
'''
가장 많은 계란을 께는 경우를 구해야함. => 브루트포스
충돌시. 무게 내구도 
my cur 내구도 - 상대 무게 <0 -> 께짐
else
update my cur 내구도

하나씩 드는데 오른쪽 계란이면 종료 => 몇개 깼나 세기.
왼쪽 달걀부터 시작.
자신을 제외한 모든 달걀을 침 + 

이차원 리스트 깊은 복사는 deep copy 사용해야한다. => 근데 시간이 너무 오래 걸린다. 사용 x
'''
import copy
N = int(input())
g_eggs =[]
for n in range(N):
    g_eggs.append(list(map(int,input().split()))) # 내구도, 무게

max_ =0


def backtracking(eggs,idx,broken_num): #idx가 손에 든 계란
    global max_
    

    
    if idx == N:
        max_ = max(max_,broken_num)
        return
    if eggs[idx][0]<=0:
        backtracking(eggs,idx+1,broken_num)
        return

    vaild = False 
    for i in range(N): #든 계란으로 i번째 달걀을 침 
        
        if i == idx: # 자기 자신은 안침
            continue
        if eggs[i][0]<=0:
            continue
        vaild = True 
        now_broken_num = broken_num
        eggs[idx][0] -= eggs[i][1]
        eggs[i][0] -= eggs[idx][1]
        if eggs[idx][0] <= 0:
            now_broken_num += 1 
        if eggs[i][0] <= 0:
            now_broken_num += 1 
        backtracking(eggs,idx+1,now_broken_num)
        eggs[idx][0] += eggs[i][1]
        eggs[i][0] += eggs[idx][1]
        
    if not vaild:
        
        backtracking(eggs,idx+1,broken_num)
            
backtracking((g_eggs),0,0)
print(max_)