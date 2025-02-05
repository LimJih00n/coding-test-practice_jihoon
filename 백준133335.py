#백준 트럭
#25.02.05 15:21 start 25.02.05 16:05 solve
#queue활용문제 => 아는 법. 순서가 일정하고 들어왔다 나가는게 보이는 경우
'''
단위시간 동안 단위길이 만큼 움직임. 
하중, 길이
순차적
길이만큼 트럭이 지나가는 데 걸림
길이만큼트럭이 올라가 있을 수 있음

다리 자체도 queue -> 무게를 쌓음

최소시간: 최대 무게에 맞게 보내야함
queue 무게보다 합이 작은 경우는 넣을 수 있음 
길이만큼 시간x
if L+next < sum bridge, => 추가 
길이가 W인 queue 생성. 0으로 
하중이 항상 <=L 이어야함 0이 나올때마다 시간 +1 
pop
마지막 차인 경우에는 0이 안들어감
마지막 차가 아닌 경우는 0 추가
따라서 다리 자체를 queue로 구성하는 것이 중요함. 차는 차, 빈칸은 0으로 구성
sum으로 합을 구해서 더 올라갈 수 잇으면 올라감. 
070 => 이런 식으로 표시!
'''
from collections import deque
N,W,L = map(int,input().split())
queue = deque()
arr = list(map(int,input().split()))
bridge = deque([0 for _ in range(W)])
for n in range(N):
    queue.append(arr[n])
time = 0
while bridge:
    time +=1
    bridge.popleft()
    
    if queue and queue[0]+sum(list(bridge))<=L:    
        bridge.append(queue.popleft())
    if queue and len(bridge)<W:
        bridge.append(0)
    
    #print(bridge)

print(time)