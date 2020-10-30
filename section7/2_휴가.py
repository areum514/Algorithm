import sys
#sys.stdin=open("../input.txt","r")

#내가 의문이 드는것은 휴가가 꼭 마지막날이 겹쳐야만 끝나는 건가..? 
def DFS(L,sum):
    global res
    if L==n+1:
        if sum>res:
            res=sum
    else: 
        if L+T[L]<=n+1:
            DFS(L+T[L],sum+P[L])    
        DFS(L+1,sum)

if __name__ == "__main__":
    n=7
    P=[]
    T=[]
    for _ in range(n):
        a,b=map(int,input().split())
        T.append(a)
        P.append(b)
    T.append(0,0)        
    P.append(0,0)
    res=0
    DFS(0,0)
    print(res)
    

