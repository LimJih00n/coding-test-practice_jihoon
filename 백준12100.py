'''
소요시간: 2시간
부족한 부분
# 문제 잘 읽기 => 한번 합쳐진 경우는 안 합쳐진다
# 구현 더 간략하게 하기 => 줄하나 잘 못쓰인 경우 답 틀림, 동일하게 모두 적용되어 있는 지 확인! => 일관성 유지
# 위로 움직이는 경우의 처리를 잘못된 곳에서 하고 있었음 => 움직임을 모두 확인하고 고치기

잘한 부분
끝까지 이동하는 것의 처리 => while문으로 검사하기
'''
import copy
N = int(input())
arr = []
re_ans = []

for i in range(N):
    arr.append(list(map(int,input().split())))
    re_ans.append(max(arr[i]))

# 5번 이동의 경우 => 4**5
# 필요없는 경우를 날려야한다. => 값이 변할 수 없는 경우를 날려야한다. 
# 전체 이동을 구현해야한다. 




move_r = [1,-1,0,0]
move_c = [0,0,1,-1]
# 아래, 위, 왼, 오 0 1 2 3
# D U L R
move_set = ("D","U","L","R")
able_move = []

def gen_h(elements, r):
    
    re = []
    
    def dfs(path):
        if len (path) == r:
            re.append(path[:])
            return
        for i in range(len(elements)):
            path.append(elements[i])
            dfs(path)
            path.pop()
    dfs([])
    return re
able_move = gen_h(move_set,5)

# 멈추는 경우 => 벽밖이거나 합쳐질 수 없는 블록이 있거나

def check_b(p):
    if p[0]>=0 and p[0]<N and p[1]>=0 and p[1]<N:
        return True
    return False

def move_simul(move_code_set):
    arr_si = copy.deepcopy(arr)
    # 오른쪽으로 이동시키는 경우
    max_num = 0
    for move_code in move_code_set:
      
        arr_be = [ [True for i in range(N)] for i in range(N) ]
        # 오른쪽으로 이동시키는 경우
        if move_code == "R":
            for c in range(N-1,-1,-1):
                for r in range(N):
                    mo = 1
                    
                    if arr_si[r][c]==0:
                        continue
                    while True:
                        new_r,new_c = r,c+mo 
                        new_p = (new_r,new_c)
                        if check_b(new_p) and arr_si[new_r][new_c]==0:
                            mo += 1
                        elif check_b(new_p) and arr_si[new_r][new_c] and arr_si[new_r][new_c] == arr_si[r][c]:
                            if arr_be[new_r][new_c] == False:
                                arr_si[new_r][new_c-1] = arr_si[r][c]
                                if not(new_r == r and new_c-1 == c):
                                    arr_si[r][c] = 0
                            else:
                                arr_si[new_r][new_c] += arr_si[r][c]
                                arr_be[new_r][new_c] = False
                                arr_si[r][c] = 0
                            max_num = arr_si[new_r][new_c] if arr_si[new_r][new_c] > max_num else max_num
                            break
                        else:
                            arr_si[new_r][new_c-1] = arr_si[r][c]
                            if not(new_r == r and new_c-1 == c):
                                arr_si[r][c] = 0
                            break
        if move_code=="L":
            for c in range(N):
                for r in range(N):
                    mo = 1
                    
                    if arr_si[r][c]==0:
                        continue
                    while True:
                        new_r,new_c = r,c-mo 
                        new_p = (new_r,new_c)
                        if check_b(new_p) and arr_si[new_r][new_c]==0:
                            mo += 1
                        elif check_b(new_p) and arr_si[new_r][new_c] and arr_si[new_r][new_c] == arr_si[r][c]:
                            if arr_be[new_r][new_c] == False:
                                arr_si[new_r][new_c+1] = arr_si[r][c]
                                if not(new_r == r and new_c+1 == c):
                                    arr_si[r][c] = 0
                            else:
                                arr_si[new_r][new_c] += arr_si[r][c]
                                arr_be[new_r][new_c] = False
                                arr_si[r][c] = 0
                            max_num = arr_si[new_r][new_c] if arr_si[new_r][new_c] > max_num else max_num
                            break
                        else: #밖으로 나가거나 안 합쳐지거나나
                            arr_si[new_r][new_c+1] = arr_si[r][c]
                            if not(new_r == r and new_c+1 == c):
                                arr_si[r][c] = 0
                            break
        if move_code=="U":
            for r in range(N):
                for c in range(N):
                    mo = 1
                    
                    if arr_si[r][c]==0:
                        continue
                    while True:
                        new_r,new_c = r-mo,c
                        new_p = (new_r,new_c)
                        if check_b(new_p) and arr_si[new_r][new_c]==0:
                            mo += 1
                        elif check_b(new_p) and arr_si[new_r][new_c] and arr_si[new_r][new_c] == arr_si[r][c]:
                            if not arr_be[new_r][new_c]:
                                arr_si[new_r+1][new_c] = arr_si[r][c]
                                if not(new_r+1 == r and new_c == c):
                                    arr_si[r][c] = 0
                            else:
                                arr_si[new_r][new_c] += arr_si[r][c]
                                arr_be[new_r][new_c] = False
                                arr_si[r][c] = 0
                            max_num = arr_si[new_r][new_c] if arr_si[new_r][new_c] > max_num else max_num
                            break
                        else:
                            arr_si[new_r+1][new_c] = arr_si[r][c]
                            if not(new_r+1 == r and new_c == c):
                                arr_si[r][c] = 0
                            max_num = arr_si[new_r][new_c] if arr_si[new_r][new_c] > max_num else max_num
                            break    
        if move_code=="D":
            for r in range(N-1,-1,-1):
                for c in range(N):
                    mo = 1
                    
                    if arr_si[r][c]==0:
                        continue
                    while True:
                        new_r,new_c = r+mo,c
                        new_p = (new_r,new_c)
                        if check_b(new_p) and arr_si[new_r][new_c]==0:
                            mo += 1
                        elif check_b(new_p) and arr_si[new_r][new_c] and arr_si[new_r][new_c] == arr_si[r][c]:
                            if not arr_be[new_r][new_c]:
                                arr_si[new_r-1][new_c] = arr_si[r][c]
                                if not(new_r-1 == r and new_c == c):
                                    arr_si[r][c] = 0
                            else:
                                arr_si[new_r][new_c] += arr_si[r][c]
                                arr_be[new_r][new_c] = False
                                arr_si[r][c] = 0
                            max_num = arr_si[new_r][new_c] if arr_si[new_r][new_c] > max_num else max_num
                            break
                        else:
                            arr_si[new_r-1][new_c] = arr_si[r][c]
                            if not(new_r-1 == r and new_c == c):
                                arr_si[r][c] = 0
                            break    
    return max_num


def move_test(move_code):
    arr_si = copy.deepcopy(arr)
    arr_be = [ [True for i in range(N)] for i in range(N) ]
    
    # 오른쪽으로 이동시키는 경우
    max_num = 0
    if move_code == "R":
        for c in range(N-1,-1,-1):
            for r in range(N):
                mo = 1
                
                if arr_si[r][c]==0:
                    continue
                while True:
                    new_r,new_c = r,c+mo 
                    new_p = (new_r,new_c)
                    if check_b(new_p) and arr_si[new_r][new_c]==0:
                        mo += 1
                    elif check_b(new_p) and arr_si[new_r][new_c] and arr_si[new_r][new_c] == arr_si[r][c]:
                        if arr_be[new_r][new_c] == False:
                            arr_si[new_r][new_c-1] = arr_si[r][c]
                            if not(new_r == r and new_c-1 == c):
                                arr_si[r][c] = 0
                        else:
                            arr_si[new_r][new_c] += arr_si[r][c]
                            arr_be[new_r][new_c] = False
                            arr_si[r][c] = 0
                        max_num = arr_si[new_r][new_c] if arr_si[new_r][new_c] > max_num else max_num
                        break
                    else:
                        arr_si[new_r][new_c-1] = arr_si[r][c]
                        if not(new_r == r and new_c-1 == c):
                            arr_si[r][c] = 0
                        break
    if move_code=="L":
        for c in range(N):
            for r in range(N):
                mo = 1
                
                if arr_si[r][c]==0:
                    continue
                while True:
                    new_r,new_c = r,c-mo 
                    new_p = (new_r,new_c)
                    if check_b(new_p) and arr_si[new_r][new_c]==0:
                        mo += 1
                    elif check_b(new_p) and arr_si[new_r][new_c] and arr_si[new_r][new_c] == arr_si[r][c]:
                        if arr_be[new_r][new_c] == False:
                            arr_si[new_r][new_c+1] = arr_si[r][c]
                            if not(new_r == r and new_c+1 == c):
                                arr_si[r][c] = 0
                        else:
                            arr_si[new_r][new_c] += arr_si[r][c]
                            arr_be[new_r][new_c] = False
                            arr_si[r][c] = 0
                        max_num = arr_si[new_r][new_c] if arr_si[new_r][new_c] > max_num else max_num
                        break
                    else: #밖으로 나가거나 안 합쳐지거나나
                        arr_si[new_r][new_c+1] = arr_si[r][c]
                        if not(new_r == r and new_c+1 == c):
                            arr_si[r][c] = 0
                        break
    if move_code=="U":
        for r in range(N):
            for c in range(N):
                mo = 1
                
                if arr_si[r][c]==0:
                    continue
                while True:
                    new_r,new_c = r-mo,c
                    new_p = (new_r,new_c)
                    if check_b(new_p) and arr_si[new_r][new_c]==0:
                        mo += 1
                    elif check_b(new_p) and arr_si[new_r][new_c] and arr_si[new_r][new_c] == arr_si[r][c]:
                        if not arr_be[new_r][new_c]:
                            arr_si[new_r+1][new_c] = arr_si[r][c]
                            if not(new_r+1 == r and new_c == c):
                                arr_si[r][c] = 0
                        else:
                            arr_si[new_r][new_c] += arr_si[r][c]
                            arr_be[new_r][new_c] = False
                            arr_si[r][c] = 0
                        max_num = arr_si[new_r][new_c] if arr_si[new_r][new_c] > max_num else max_num
                        break
                    else:
                        arr_si[new_r+1][new_c] = arr_si[r][c]
                        
                        if not(new_r+1 == r and new_c == c):
                            arr_si[r][c] = 0
                        max_num = arr_si[new_r][new_c] if arr_si[new_r][new_c] > max_num else max_num
                        break    
    if move_code=="D":
        for r in range(N-1,-1,-1):
            for c in range(N):
                mo = 1
                
                if arr_si[r][c]==0:
                    continue
                while True:
                    new_r,new_c = r+mo,c
                    new_p = (new_r,new_c)
                    if check_b(new_p) and arr_si[new_r][new_c]==0:
                        mo += 1
                    elif check_b(new_p) and arr_si[new_r][new_c] and arr_si[new_r][new_c] == arr_si[r][c]:
                        if not arr_be[new_r][new_c]:
                            arr_si[new_r-1][new_c] = arr_si[r][c]
                            if not(new_r-1 == r and new_c == c):
                                arr_si[r][c] = 0
                        else:
                            arr_si[new_r][new_c] += arr_si[r][c]
                            arr_be[new_r][new_c] = False
                            arr_si[r][c] = 0
                        max_num = arr_si[new_r][new_c] if arr_si[new_r][new_c] > max_num else max_num
                        break
                    else:
                        arr_si[new_r-1][new_c] = arr_si[r][c]
                        if not(new_r-1 == r and new_c == c):
                            arr_si[r][c] = 0
                        break    
    print_arr(arr_si)
    
def print_arr(p_arr):
    for i in range(N):
        print(p_arr[i])
    print("==")

for move_code_set in able_move:
    re_ans.append(move_simul(move_code_set))
print(max(re_ans))

#move_test("D")
#move_test("U")
#move_test("L")
#move_test("R")
    

