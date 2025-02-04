#백준 13023
#ABCDE
#25.02.04 13:30start 14:24 end
'''
친구 관계. => 그래프가 모두 연결되어있는지 확인 x
ABCDE가 무엇인지 이해하는 게 중요함. 
간선 4개. 길이가 4인 친구가 있냐 없냐임. 
모든 노드 path. 탐색, 길이가 4인 친구 생기면1 끝까지 다봤는데 없으면 0
dfs로 모든 노드 탐색, 길이 담아서 
실수1: 단방향으로 함. 수정함.
26퍼에서 틀림. 머지? => 방문하기전에도 add함
50%에서 틀림.

길이가 끝난 경우에 pop해주는 과정을 해야한다. 3에서 끝나면 4로 가는 경우를 못찾는다.
원래 생각. 각 visit가 독립적이라 생각함. 모든 path를 봐야한다!
실패한 경우 원래 방문을 없에는 것이 필요 => set.remove() or set.discard()
'''
N,M = map(int,input().split())
ad_list={}
for i in range(N):
    ad_list[i] = []

for _ in range(M):
    a,b = map(int,input().split())
    ad_list[a].append(b)
    ad_list[b].append(a)


def dfs(node,visit,dis):
    visit.add(node)
    #print(node,"방문!",dis)
    if dis==4:
        return True
    
    for ne in ad_list[node]:
        if ne not in visit:
            visit.add(ne)
            if dfs(ne,visit,dis+1):
                return True
    visit.discard(node)
            
    return False
ans = 0
#print(ad_list)
for node in ad_list.keys():
    #print(node,"시작!")
    if dfs(node,set(),0):
        ans=1
print(ans)