import sys
#sys.stdin=open("../input.txt","r")

def DFS(L,amount,cnt):
    global result
    
    if L==m:
        return
    if cnt>result:
        return
    if amount==0:
        if cnt<result:
            result=cnt
        
    else: 
        for i in range(0,n):
            if ch[i]==0:
                ch[i]=1
                cnt+=amount//a[L]
                amount=amount%a[L]
                res[i]=a[L]
                DFS(L+1,amount,cnt)
                ch[i]=0


if __name__ == "__main__":
    n=int(input())
    a=list(map(int,input().split()))
    m=int(input())
    ch=[0]*n
    res=[0]*n
    a.sort(reverse=True)
    cnt=0
    result=2147000000
    DFS(0,m,0)
    print(result)