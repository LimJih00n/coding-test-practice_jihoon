#2025.21.25 start
'''
힌트 보고 해결
but 개 어이없게 틀림. 조합 구성을 잘못짬. 알고리즘 잘 이해하기
+ 경우 나오는 거 작은 테스트 case라도 만들어서 봐야함. 실전에서는 
접근은 맞음. 
더 빨라야한다면 -> 집 - 치킨 거리를 리스트로 만들고. 경우를 뽑아서 각값을 더하는 식으로 하면 더 빨라질 듯 함. over되면 줄이는 경우도 ㄱㅊ
'''


# NxN 칸. 도시칸은 0:빈칸, 1:집, 2: 치킨집
# r,c 1부터 시작!
# 치킨거리: 집과 가장 가까운 치킨집 사이의 거리 => 가로세로길이임
#도시의 치킨거리: 모든집의 치킨 거리의 합
# m개 닫아야함. 도시의 치킨거리가 가장 작게될 경우 찾기
# => 브루트포스 => 순열 조합 중복순열 구하기 => 다시 공부 
# 전략
# 폐업 시킬 수 있는 모든 경우 구하기 => 조합. 구하기
# 폐업 시킨 후 거리 구하기
# 최소 거리 찾기

# 구현해야하는 함수1 : 폐업 경우 구하기 => gen_c => 
# 구현함수2: 거리 구하는 함수 (bfs or dfs) bfs로 탐색. 가장 가까운 거리 찾으면 끝. 거리는 어디에 저장?
# 굳이 그럴 필요가 없다. 집 거리에서 빼면된다. 공식을 줌. bfs를 사용하는 경우는 고불 고불 가야하는 경우가 있는 경우다.
# 폐업한 경우를 제외한 경우 구하기
# 전체 집과 폐업한 치킨집 제외 집간의 거리 구하기. 
# 폐업 시킬 수 있는 치킨집의 수가 최대 M개이다. =>x
# 폐업 시키지 않을 치킨집의 개수가 최대 M개. 즉 M개 까지 있을 수 있음 

# O(chicn-M)
#  폐업 경우에 대해 반복 => O(M)
#   => 치킨집 하나 선택 => 전체 집과의 거리계산. 가작 작은 것 택하기 => O(2N) 모든집의 거리다.
# 치킨집과의 거리가 아니라. 모든집 관점!
# 각 경우의 sum 합하기 => 이 합들 중 최소값 구하기. 

# 반복문 3개 시간 초과 나옴.
from collections import deque

def cal_dis(node1,node2):
    return abs(node1[0]-node2[0]) + abs(node1[1]-node2[1])

arr = []
able_t = []
house_p=[]
dr = [1,-1,0,0]
dc = [0,0,1,-1]

N,M = map(int,input().split())
for i in range(N):
    row = list(map(int,input().split()))
    arr.append(row)
    
house_p = [(r,c) for r in range(N) for c in range(N) if arr[r][c] == 1]
able_t =  [(r,c) for r in range(N) for c in range(N) if arr[r][c] == 2]



def gen_c(elements,r):
    re = []
    def dfs(s,path):
        if len(path) == r:
            re.append(path[:])
            return
        for i in range(s,len(elements)):
            path.append(elements[i])
            dfs(i+1,path)
            path.pop()
    dfs(0,[])
    return re  


    

able_case = gen_c(able_t,M)

# 집 to chcik
# 현재 모든 폐업 안된 case에 대해 
# 집 - chi => 최소값을 찾은 경우 더 반복할 필요는
# 모든 집이 그 case를 모두 확인한다. 
min_dis = float("inf")
for ch_cases in able_case:
    city_dis = 0
    for h_case in house_p:
        city_dis += min(cal_dis(case,h_case) for case in ch_cases)
        if city_dis> min_dis:
            break
    min_dis = min(min_dis,city_dis)

print(min_dis)
