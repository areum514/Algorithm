import sys
#sys.stdin=open('../input.txt','r')
def DFS(L,sum):
    global total
    global half_total
    if sum>half_total:
        return
    if L==n:
        if half_total==sum:
            print('YES')
            sys.exit(0)
    else:
        DFS(L+1,sum+a[L])
        DFS(L+1,sum)
        
if __name__ == "__main__":
    n=int(input())
    a=list(map(int,input().split()))
    total=sum(a)
    half_total=total/2
    DFS(0,0)
    print('NO')