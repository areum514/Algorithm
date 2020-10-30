import sys
sys.stdin=open("../input.txt","r")
def DFS(v):
    global res
    if v==m:
        for x in res:
            print(x,end=" ")
        print()
    else:
        for i in range(1,n+1):      
            if ch[i]==0:
                ch[i]=1
                res[v]=i     
                DFS(v+1)
                ch[i]=0

if __name__ == "__main__":
    n,m=map(int,input().split())
    res=[0]*m
    ch=[0]*(n+1)
    DFS(0)