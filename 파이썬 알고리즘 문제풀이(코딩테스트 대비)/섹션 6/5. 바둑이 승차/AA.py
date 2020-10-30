import sys
#sys.stdin=open('../input.txt','r')
def DFS(L,sum,tsum):
    global result
    global total
    if sum+(total-tsum)<result:
        return
    if sum>c:
        return
    if L==n:
        if sum>result:
            result=sum
    else: 
        DFS(L+1,sum+a[L],tsum+a[L])
        DFS(L+1,sum,tsum+a[L])
        
if __name__ == "__main__":
    c, n=map(int,input().split())
    a=[int(input()) for _ in range(n)]
    result=-217000000
    total=sum(a)
    DFS(0,0,0)
    print(result)
    