import copy
move_r = [1,-1,0,0]
move_c = [0,0,1,-1]
R,C = map(int,input().split())
arr = []
zero_init_po=[]
#dfs 가능 => 모두 봐야하는 경우이기때무
    

for r in range(R):
    arr.append(list(map(int,input().split())))

zero_init_po = [(r,c) for r in range(R) for c in range(C) if arr[r][c]==0]
bi_init_po =  [(r,c) for r in range(R) for c in range(C) if arr[r][c]==2]

def gen_c(elements, r):
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

able_wall = gen_c(zero_init_po,3)   

def one_con(po1,po2,po3):
    arr_si = copy.deepcopy(arr)
    
    arr_si[po1[0]][po1[1]] = 1
    arr_si[po2[0]][po2[1]] = 1
    arr_si[po3[0]][po3[1]] = 1
    
    visted = set()


    def bi_move(node): # 다 채우는 경우
        if node not in visted and arr_si[node[0]][node[1]]:
            visted.add(node)
            for i in range(4):
                new_node = (node[0] + move_r[i] , node[1] + move_c[i])
                if new_node[0]>=0 and new_node[1]>=0 and new_node[0] <R and new_node[1]<C and arr_si[new_node[0]][new_node[1]]==0:
                    arr_si[new_node[0]][new_node[1]] = 2
                    bi_move(new_node)
    
    for po in bi_init_po:
        bi_move(po)
    

                
    save_arr = sum([1 for i in range(R) for j in range(C) if arr_si[i][j]==0])
    return save_arr
    
ans= []

for po1,po2,po3 in able_wall:
    ans.append(one_con(po1,po2,po3))

print(max(ans),end="")
    


# 생각을 먼저하고 풀자
# 연구원
# 벽을 세우는 문제 다 세워야한다 => 경우를 구하고 세우고 => 바이러스 돌리고 => 
# 1. map 입력 받기
# 2. 0의 위치 구하기