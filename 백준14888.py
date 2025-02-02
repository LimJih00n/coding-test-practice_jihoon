'''
문제 조건 꼼꼼하게 보기
30분 정도 걸림
'''
import copy
N = int(input())
arr = list(map(int,input().split()))
oper_arr = list(map(int,input().split()))

# 배치의 모든 경우 구해야함
# 계산의 모든 결과 구해야함

able_op_set = []
op_l = [0,1,2,3]
def gen_h(elements,r):
    re = []
    used_op = copy.deepcopy(oper_arr)
    
    def dfs(path,used_op):
        
        if len(path) == r:
            re.append(path[:])
            return
        
        for i in range(len(elements)):
            
            if used_op[i] >0:
                path.append(elements[i])
                used_op[i] -=1
                dfs(path,used_op)
                used_op[i] +=1
                path.pop()
    dfs([],used_op)
    return re 

able_op_set = gen_h(op_l,N-1)
ans = []
#print(able_op_set)
for op_code_s in able_op_set:
    re = arr[0]
    for i in range(0,len(arr)-1):
        
        if op_code_s[i] == 0:
            re += arr[i+1]
        elif op_code_s[i] == 1:
            re -= arr[i+1]
        elif op_code_s[i] == 2:
            re *= arr[i+1]
        elif op_code_s[i] == 3:
            if re<0:
                re*=-1
                re //=arr[i+1]
                re *=-1
            else:
                re //= arr[i+1]
    ans.append(re)
print(max(ans))
print(min(ans))