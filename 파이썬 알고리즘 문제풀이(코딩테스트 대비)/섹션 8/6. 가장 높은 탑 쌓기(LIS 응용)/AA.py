import sys

#sys.stdin=open('../input.txt','r')

n=int(input())
brick_info=list()
for i in range(n):
    a,b,c=map(int,input().split())
    brick_info.append([a,b,c])

brick_info.sort()
dy=[0]*n
dy[0]=brick_info[0][1]
res=0
for i in range(1,n):
    max=0
    for j in range(i):
        if brick_info[i][2]>brick_info[j][2] and dy[j]>max:
            max=dy[j]
    dy[i]=max+brick_info[i][1]
    if dy[i]>res:
        res=dy[i] 

print(res)




