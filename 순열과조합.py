# 순열 조합 중복순열
# path에 경우를 담는 것이 목표임

def gen_c(elements,r):
    
    re = []
    
    
    def dfs(start,path): # index로 중복안되게
        
        if len(path) == r:
            re.append(path[:])
            return
        
        for i in range(start,len(elements)): #다음꺼에서 가능한 조합을 찾음
            path.append(elements[i])
            dfs(i+1,path)
            path.pop()

    dfs(0,[])
    return re

def gen_p(elements,r):
    re = []
    used = [False] *len(r) # 사용한 거를 구분함
    
    def dfs(path):
        if len(path) == r:
            re.append(path[:])
            return
        
        for i in range(len(elements)):
            
            if not used[i] :
                path.append(elements[i])
                
                used[i] = True # 사용했다고 하고
                dfs(path) # 끝까지 가는 경우 => 순열
                used[i] = False
                path.pop()
    dfs([])
    return re

def gen_h(elements,r):
    re = []
    used = [False] *len(r) # 사용한 거를 구분함
    
    def dfs(path):
        if len(path) == r:
            re.append(path[:])
            return
        
        for i in range(len(elements)):
            
            if not used[i] :
                path.append(elements[i])
                
                dfs(path) # 사용 표시를 다끝나고 하는 경우 => 중복순열
                used[i] = False
                path.pop()
    dfs([])
    return re

# 복습
# 순열, 조합, 중복순열
# 순열 => path 제귀적으로 담는데, elements의 길이 visted로 방문한 경우 를 표시함 => path를 매개변수로
# 조합 => path 제귀적으로 담는데 index두어서 이를 무시 => path, index를 매개변수로
# 순열 => path 제귀적으로 담는데, visted 방문결과가 없음 => 

