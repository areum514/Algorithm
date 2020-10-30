import sys
#sys.stdin=open('../input.txt',"r")
dx=[-1,0,1,0]
dy=[0,1,0,-1]
def DFS(a,b):
    global cnt
    if a==6 and b==6:
        cnt+=1
    else: 
        for i in range(4):
            x=a+dx[i]
            y=b+dy[i]
            if 0<=x<=6 and 0<=y<=6 and board[x][y]==0:
                board[x][y]=1
                DFS(x,y)
                board[x][y]=0

if __name__ == "__main__":
    board=[list(map(int,input().split())) for _ in range(7)]
    board[0][0]=1
    cnt=0   
    DFS(0,0)
    print(cnt)
    
