import sys
#sys.stdin=open('../input.txt','r')

if __name__ == "__main__":
    n=int(input())
    coin =list(map(int,input().split()))
    w=int(input())
    coin.sort(reverse=True)
    dy=[1000]*(w+1)
    dy[0]=0
    for x in coin:
        for j in range(x,w+1):
            dy[j]=min(dy[j],dy[j-x]+1)
    print(dy[-1])
        

    