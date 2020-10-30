import sys

sys.stdin=open('./input.txt','r')
dx=[-1,0,1,0]
dy=[0,1,0,-1]
def DFS(x,y):
    global cnt
if __name__ == "__main__":
    n=int(input())
    a=[list(map(int,input().split())) for _ in range(n)]
    print(a)
