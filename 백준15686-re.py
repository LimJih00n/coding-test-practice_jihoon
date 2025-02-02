# 빠른 기법 적용해서 새로 풀어보기


def gen_c(elements, r):
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
N,M = map(int,input().split())
arr = [list(map(int,input().split())) for r in range(N) ]
chic = [(r,c) for r in range(N) for c in range(N) if arr[r][c]==2]
house = [(r,c) for r in range(N) for c in range(N) if arr[r][c]==1]

dis_set = []

def cal_dis(node1,node2):
    return abs(node1[0]-node2[0]) + abs(node1[1]-node2[1])

dis_set = [ [cal_dis(h,c) for c in chic ] for h in house]
el = [i for i in range(len(chic))]
able_set = gen_c(el,M)
ans_dist = float("inf")
for case in able_set:
    city_dis = 0
    for h in range(len(house)):
        
        city_dis += min(dis_set[h][c] for c in case)
        if city_dis >= ans_dist:
            break
    ans_dist = min(city_dis,ans_dist)

print(ans_dist)