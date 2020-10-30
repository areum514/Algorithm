import sys

#sys.stdin=open('../input.txt','r')
dx=[-1,0,1,0]
dy=[0,1,0,-1]
def DFS(x,y):
    global cnt
    if x==max_x and y==max_y:
        cnt+=1
    else:
        for i in range(4):
            xx=x+dx[i]
            yy=y+dy[i]
            if 0<=xx<n and 0<=yy<n and a[x][y]<a[xx][yy]:
                ch[xx][yy]=1
                DFS(xx,yy)
                ch[xx][yy]=0
if __name__ == "__main__":
    n=int(input())
    a=[list(map(int,input().split())) for _ in range(n)]
    ch=[[0]*n for _ in range(n)]
    cnt=0
    min_x=100
    min_y=100
    min_n=100

    max_x=0
    max_y=0
    max_n=0
    for i in range(n):
        for j in range(n):
            if min_n>a[i][j]:
                min_x=i
                min_y=j
                min_n=a[i][j]
            if max_n<a[i][j]:
                max_x=i
                max_y=j
                max_n=a[i][j]
    ch[min_x][min_y]=1
    DFS(min_x,min_y)
    print(cnt)
    

