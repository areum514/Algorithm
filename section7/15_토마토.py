import sys
from collections import deque

sys.stdin=open('../input.txt','r')
dx=[-1,0,1,0]
dy=[0,1,0,-1]

if __name__ == "__main__":
    n,m=map(int,input().split())
    board=[list(map(int,input().split())) for _ in range(m)]
    ch=[[0]*n for _ in range(m)]
    Q=deque()
    
    for i in range(m):
        for j in range(n):
            if board[i][j]==1:
                Q.append((i,j))
    while Q:
        tmp=Q.popleft()
        for k in range(4):
            x=tmp[0]+dx[k]
            y=tmp[1]+dy[k]
            if 0<=x<m and 0<=y<n and board[x][y]==0:
                ch[x][y]=ch[tmp[0]][tmp[1]]+1
                board[x][y]=1
                Q.append((x,y))

    flag=1
    for i in range(m):
        for j in range(n):
            if board[i][j]==0:
                flag=0
    result=0
    if flag==1:
        for i in range(m):
            for j in range(n):
                if ch[i][j]>result:
                    result=ch[i][j]
        print(result)
    else: 
        print(-1)

    

                    

""" if __name__ == "__main__":
    n,m=map(int,input().split())
    board=[list(map(int,input().split())) for _ in range(m)]
    ch=[[0]*n for _ in range(m)]
    Q=deque()
    for x in board:
        print(x)
    print()
    for i in range(m):
        for j in range(n):
            if board[i][j]==1 and ch[i][j]==0:
                ch[i][j]=1
                Q.append((i,j))
    while Q:
        tmp=Q.popleft()
        for k in range(4):
            x=tmp[0]+dx[k]
            y=tmp[1]+dy[k]
            if 0<=x<m and 0<=y<n and board[x][y]==0:
                board[x][y]=1
    
    for x in board:
        print(x)
 """
            