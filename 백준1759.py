#백준 1759
# 암호 만들기
# start: 25.02.02 13:00 
# solve: 25.02.02 13:40 
# 길이가 L, 문자 종류가 C
# 최소 하나의 모음, 최소 2개의 자음으로 구성되어야함
# 알파벳 정렬 순. => 대소 비교. 길이가 정해진 backtracking, & 안되는 경우는 컷
# 그냥 길이가 L인 조합 생성하기. 인데. 조건을 안넣었다.
# 입력 받은 문자를 정렬하고 시작하면 되기는하다. 
# 모든 암호 출력하기.

L,C = map(int,input().split())
arr = sorted(list(input().split()))
gather = ['a','e','i','o','u']
consonent = list(filter(lambda x: x not in gather, arr))
#print(consonent)
#print(arr)

def gen_c(ele,r):
    re = []
    def dfs(path,s):
        if len(path) == r:
            #print(set(consonent) & set(path))
            if len(set(gather) & set(path))>=1 and len(set(consonent) & set(path))>=2:
                re.append(path[:])
                
            return
        for i in range(s,len(ele)):
            path.append(ele[i])
            dfs(path,i+1)
            path.pop()
    dfs([],0)
    return re
cases = gen_c(arr,L)
for ans in cases:
    print("".join(ans))
            
