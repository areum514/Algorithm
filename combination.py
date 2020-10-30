def DFS(L,s):
    global cnt
    global res
    if L==m:
        cnt+=1
        print(res)
    else: 
        for i in range(s,n):
            res[L]=i
            DFS(L+1,i+1)

if __name__ == "__main__":
    n=4
    m=2
    res=[0]*m
    cnt=0
    DFS(0,1)
    print(cnt)