import sys

def DFS(v):
    global res
    if v==n:
        answer=list(res)
        
        for i in range(n-1,0,-1):
            for j in range(i):
                answer[j]+=answer[j+1]
                if answer[0]> k:
                    return
        if answer[0]==k:
            for x in res:
                print(x,end=" ")
            sys.exit(0)
        
    else:
        for i in range(n):
            if c[i]==0:
                c[i]=1
                res[v]=i+1
                DFS(v+1)
                c[i]=0
        



if __name__ == "__main__":
    #sys.stdin=open("../input.txt","r")
    n,k=map(int,input().split())
    c=[0]*n
    res=[0]*n
    cnt=0
    DFS(0)
    print(cnt)

