import sys


def DFS(L,s,sum):
    global cnt
    if L==k:
        if sum%m==0:
            cnt+=1
    else:
        for i in range(s,n):
            DFS(L+1,i+1,sum+a[i])
    
    

if __name__ == "__main__":
    sys.stdin=open("../input.txt","r")
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    m=int(input())
    cnt=0
    res=[0]*k
    DFS(0,0,0)
    print(cnt)
    