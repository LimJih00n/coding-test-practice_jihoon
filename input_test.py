N = int(input())
arr =[]
for i in range(N):
    arr.append(list(map(int,input().split())))
R1,C1 = map(int,input().split())
R2,C2 = map(int,input().split())
R3,C3 = map(int,input().split())
con = [(R2,C2),(R3,C3)]
move_r = [1,-1,0,0]
move_c = [0,0,1,-1]
visted = set()

def check_b(r,c):
    if r<=N and c<=N and r>0 and c>0:
        return True
    return False
count = 0
def dfs(node):
    global count
    if node not in visted:
        visted.add(node)

        for i in range(4):
            new_node = (node[0]+move_r[i],node[1]+move_c[i])
        
            if new_node not in visted and check_b(node[0]+move_r[i],node[1]+move_c[i]) and arr[new_node[0]-1][new_node[1]-1] :
                if new_node in con:
                    count += 1
                dfs(new_node)
dfs((R1,C2))
if count == 2:
    print(1)
else:
    print(0)


    