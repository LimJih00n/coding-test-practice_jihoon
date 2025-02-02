#백준 1182
#25.01.28.22.43 start 22.58 stop
#25.02.02.12.14 start 
#부분수열 합 구하기 => 브루트포스.
# N개의 수열에서 합이 S가 되는 경우를 구해야함
# 수열 자르는 것을 계산해야함 S가 안되는 경우를 컷해야함 => 더 진행안해야함
# 길이에 따라 나누기. 
# N, N-1, N-2, N-3
# 틀림 => 이유: 연속하지 않아도 됨. 
# 즉 순서만 맞으면 되는 것임..
# 1 2 3 4 에서  1 3 도 가능. 
# 합이 양수인 부분 수열만 본다. 
# 1 2 3 4
# 1 3 4. 어짜피 합이기 때문에 조합으로 쭉 뽑으면 됨.

# 모든 경우 다하기.
N,S = map(int,input().split())
arr = list(map(int,input().split()))
count = 0

ans =[]
def back(start):
    global count
    
    if sum(ans) == S and len(ans)>0:
        count += 1
    
    for i in range(start,len(arr)):
        ans.append(arr[i])
        back(i+1)
        ans.pop()

back(0)
print(count)