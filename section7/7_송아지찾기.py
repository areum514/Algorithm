import sys
from collections import deque

sys.stdin=open('./input.txt','r')
n,m=map(int,input().split())
MAX=1000
ch=[0]*(MAX+1)
dis=[0]*(MAX+1)
ch[n]=1
dQ=deque()
dQ.append(n)
while dQ:
    now=dQ.popleft()
    if now==m:
        break
    for next in (now-1,now+1,now+5):
        if 0<next<=MAX and ch[next]==0:
            dQ.append(next)
            ch[next]=1
            dis[next]=dis[now]+1
print(dis[m])
