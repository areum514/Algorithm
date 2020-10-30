import sys
import itertools as it


def DFS(L,s):
    global cnt
    if L==m:
        cnt+=1
        for x in range(L):
            print(res[x], end=" ")
        print()
    else:
        for i in range(s,n):
            res[L]=a[i]
            DFS(L+1,i+1)
    

if __name__ == "__main__":
    sys.stdin=open("../input.txt","r")
    n,m=map(int,input().split())
    a=[2, 4, 5, 8, 12]
    res=[0]*n
    cnt=0
    DFS(0,0)
    print(cnt)
"""
def DFS(L):
    global cnt
    if L==m:
        cnt+=1
        for x in range(1,m+1):
            print(res[x], end=" ")
        print()
    else:
        for i in range(1,n+1):
            if c[L]==0 and res[L]<i:
                c[L]=1
                res[L+1]=i
                DFS(L+1)
                c[L]=0
    
        
if __name__ == "__main__":
    sys.stdin=open("../input.txt","r")
    n,m=map(int,input().split())
    c=[0]*n
    res=[0]*(m+1)
    cnt=0
    DFS(0)
    print(cnt)


 """