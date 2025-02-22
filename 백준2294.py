#백준 2294
'''
25.02.22 17:30 start 18:00 solve
# k를 만드는 데 필요한 동전의 개수 => coin(j)을 사용할때. k - j랑 같음. 
동전의 개수를 최소로
# 즉 k-j가 최소이면 경우의 수 역시 최소임
1의 경우 경우의 수를 저장함
지금은 사용한 최소 동전의 수를 저장해야함.


case[x] = x를 만들때 사용한 최소 동전의 수
case[x-coin] => coin을 사용하면 됨
즉 + 1
case[x] = case[x-coin] + 1
최소를 보장해줘야함

동전 가치가 100,000 임 max
'''

n,k = map(int,input().split())
coins = [int(input()) for _ in range(n)]

case_ = [-1 for _ in range(100001)]
for c in coins:
    case_[c] = 1


for coin in coins:
    for j in range(coin, k+1):
        if  j-coin>=0:
            if case_[j] != -1 and case_[j-coin] != -1:
                case_[j] = min(case_[j-coin] + 1,case_[j]) # 현재의 경우와 이 코인을 사용했을때의 경우 중 코인을 덜 사용한 것을 넣음
            elif case_[j-coin] != -1: # 즉 만들 수 있는 경우 
                case_[j] = case_[j-coin] + 1  # 
            
        
print(case_[k])
        
