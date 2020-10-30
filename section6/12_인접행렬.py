import sys

def DFS():
    pass

if __name__ == "__main__":
    sys.stdin=open("../input.txt","r")
    n,m=map(int,input().split())
    a=[[0]*n for _  in range(n)]
    for _ in range(m):
        i,j,x=map(int,input().split())
        a[i-1][j-1]=x
    for x in a:
        for k in x:
            print(k,end=" ")
        print()