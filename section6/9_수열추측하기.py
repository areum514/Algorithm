import sys
import itertools as it
def DFS(L,sum):
    global res
    if L==n and k==sum:
        for x in res:
            print(x , end=" ")
        sys.exit(0)
        
    else:
        for i in range(n):
            if c[i]==0:
                c[i]=1
                res[L]=i+1
                DFS(L+1,sum+(res[L]*b[L]))
                c[i]=0
        
if __name__ == "__main__":
    sys.stdin=open("../input.txt","r")
    n,k=map(int,input().split())
    c=[0]*n
    res=[0]*n
    b=[1]*n
    for i in range(1,n):
        b[i]=(b[i-1]*(n-i))/i
    DFS(0,0)
    """ for tmp in it.permutations(a):
        sum=0
        for L,x in enumerate(tmp):
            sum+=(x*b[L])
        if sum==f:
            for x in tmp:
                print(x,end=" ")
            break """

