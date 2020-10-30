import sys
sys.stdin=open('../input.txt','r')
#스택에 매개변수, 지역변수, 복귀주소 main 13째줄, DFS(3)의 9번째줄 DFS(2)의 9번째줄 이렇게..! 
def DFS(x):
    if x==0:
        return
    else:
        DFS(x//2)
        print(x%2,end="")
if __name__ == "__main__":
    n=int(input())
    DFS(n)