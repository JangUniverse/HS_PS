import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

# strongly connected component 티스토리
def scc(g,v):
    finished=[False]*(v+1)
    label=[0] # 누적 라벨 : 노드를 한번 방문 할때마다 1씩 증가
    labels=[0]*(v+1) 
    ans,s=[],[]
    
    def _scc(u):
        label[0]+=1
        parent=labels[u]=label[0]
        s.append(u)
        
        for v in g[u]:
            if not labels[v]:
                
                parent=min(parent,_scc(v))
            elif not finished[v]:
                # 방문 했었으나 scc처리가 아직 안된 노드 = 사이클
                parent=min(parent,labels[v])
        if parent==labels[u]:
            # 자기 자신이 사이클 중 가장 먼저 탐색= 루트노드
            scc_set=[]
            while s:
                p=s.pop()
                scc_set.append(p)
                finished[p]=True
                if u==p:
                    break
            ans.append(scc_set)
        return parent
    
    for e in range(1,v+1):
        if not labels[e]:
            _scc(e)
    
    return ans

v,e=map(int,input().rstrip().split())
g=[list() for _ in range(v+1)]
for _ in range(e):
    u,vv=map(int,input().rstrip().split())
    g[u].append(vv)

ans=scc(g,v)
for e in ans:
    e.sort()
ans.sort(key=lambda e: e[0])

print(len(ans))

for e in ans:
    res=''
    for _e in e:
        res+=str(_e)+' '
    res+='-1'
    print(res)