import sys
sys.stdin=open('../input.txt','r')
def DFS(x):
    global ch
    if x==n+1:
        for i in range(len(ch)):
            if ch[i]==1:
                print(i,end=" ")
        print()
    else:
        ch[x]=1
        DFS(x+1)
        ch[x]=0
        DFS(x+1)
        
if __name__ == "__main__":
    n=int(input())
    ch=[0]*(n+1)
    DFS(1)