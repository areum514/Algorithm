import sys

sys.stdin=open('../input.txt',"r")
def DFS(L):
    if dy[L]>0:
        return dy[L]
    if L==1 or L==2:
        return L
    else:
        dy[L]=DFS(L-1)+DFS(L-2)
        return dy[L]
if __name__ == "__main__":
    n=int(input())
    dy=[0]*(n+1)
    print(DFS(n))


