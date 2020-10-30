import sys
#sys.stdin=open("../input.txt","r")
def DFS(L,sum):
    global cnt
    if sum>t:
        return
    if L==k:
        if sum==t:
            cnt+=1
        return
    else:
        for i in range(cn[L]+1):
            DFS(L+1,sum+cv[L]*i)




if __name__ == "__main__":
    t=int(input())
    k=int(input())
    cv=list()
    cn=list()
    for i in range(k):
        num,count =map(int,input().split())
        cv.append(num)
        cn.append(count)
    cnt=0
    DFS(0,0)
    print(cnt)
