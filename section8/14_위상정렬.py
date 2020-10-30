import sys
from collections import deque
sys.stdin=open('../input.txt','r')

if __name__ == "__main__":
    n,m=map(int,input().split())
    degree=[0]*(n+1)
    dis=[[0]*(n+1) for _ in range(n+1)]
    for i in range(1,m+1):
        a,b=map(int,input().split())
        dis[a][b]=1
        degree[b]+=1
    
    que=deque()
    
    for i in range(1,n+1):
            if degree[i]==0:
                que.append(i)

    while que:
        now=que.popleft()
        for i in range(1,n+1):
            if dis[now][i]==1:
                degree[i]-=1
                if degree[i]==0:
                    que.append(i)
        print(now, end=" ")


