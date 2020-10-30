import sys
from collections import deque

sys.stdin=open('./input.txt','r')
board=list( list(map(int,input().split())) for _ in range(7))
dis=[[0]*7 for _ in range(7)]
Q=deque()
dx=[1,0,-1,0]
dy=[0,-1,0,1]
Q=deque()
Q.append((0,0))
board[0][0]=1
while Q:
    tmp=Q.popleft()
    for i in range(4):
        x=tmp[0]+dx[i]
        y=tmp[1]+dy[i]
        if 0<=x<7 and 0<=y<7 and board[x][y]==0:
            board[x][y]=1
            dis[x][y]=dis[tmp[0]][tmp[1]]+1
            Q.append((x,y))
print(dis)
if dis[6][6]==0:
    print(-1)
else:
    print(dis[6][6])
