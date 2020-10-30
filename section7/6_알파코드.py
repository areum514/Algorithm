import sys
sys.stdin=open('./input.txt','r')

def DFS(L,P):
    global cnt
    if L==n:
        cnt+=1
        for j in range(P):
            print(res[j],end=" ")
        print()
    else:
        for i in range(1,27):
            if CODE[L]==i:
                res[P]=i
                DFS(L+1,P+1)
            elif i>=10and CODE[L]==i//10 and CODE[L+1]==i%10:
                res[P]=i
                DFS(L+2,P+1)
if __name__ == "__main__":
    CODE=list(map(int,input()))
    n=len(CODE)
    CODE.insert(n,-1)
    cnt=0
    res=[0]*(n+3)
    DFS(0,0)
    print(cnt)