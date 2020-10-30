import sys
sys.stdin=open('../input.txt','r')
dx=[0,0,-1]
dy=[-1,1,0]

def DFS(x,y):
    if x==0:
        print(y)
    else:
        for i in range(3):
            xx=x+dx[i]
            yy=y+dy[i]
            if 0<=xx<10 and 0<=yy<10 and ch[xx][yy]==0 and baord[xx][yy]==1:
                ch[xx][yy]=1
                DFS(xx,yy)
                break
            

if __name__ == "__main__":
    n=10
    baord=[list(map(int,input().split())) for _ in range(n)]
    ch=[[0]*n for _ in range(n)]
    for i in range(n):
        if baord[9][i]==2:
            ch[9][i]=1
            DFS(9,i)
            break