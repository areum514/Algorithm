import sys
sys.stdin=open('../input.txt','r')

n,m=map(int,input().split())
dis=[[100]*(n+1) for _ in range(n+1)]
for i in range(1,n+1):
    dis[i][i]=0
for i in range(m):
    a,b,c=map(int,input().split())
    dis[a][b]=c
for k in range(1,n+1):
    for i in range(1,n+1):
        for j in range(1,n+1):
            dis[i][j]=min(dis[i][j],dis[i][k]+dis[k][j])
for i in range(1,n+1):
    for j in range(1,n+1):
        if dis[i][j]==100:
            print('M',end=" ")
        else:
            print(dis[i][j],end=" ")
    print()