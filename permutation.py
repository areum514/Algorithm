def DFS(L):
    global cnt
    if L==4:
        cnt+=1
        print(a)
    else: 
        for i in range(4):
            if ch[i]==0:
                ch[i]=1
                a[L]=i
                DFS(L+1)
                ch[i]=0

if __name__ == "__main__":
    n=4
    ch=[0]*4
    a=[0]*4
    cnt=0
    DFS(0)
    print(cnt)