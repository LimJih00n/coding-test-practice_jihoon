'''
12.20.19.40 시작

총감독관을 빼고 몫만큼 더해야하는 문제, 나누어떨어질 경우를 주의

'''

N = int(input())
arr = list(map(int,input().split()))
B,C = map(int,input().split())


chef_di = len(arr)
sub_dir = 0
for i in range(len(arr)):
    arr[i] -= B
    if arr[i]<=0:
        continue
    sub_dir = sub_dir + arr[i] // C  if arr[i]%C==0 else sub_dir + (arr[i] // C) +1
print(chef_di+sub_dir)
    
        
    