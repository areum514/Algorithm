import sys
sys.stdin=open("input.txt","r")

n=int(input())
n_list=[]
n_list=list(map(int,input().split()))
n_list.sort()
m=int(input())
for i in range(m):
    n_list[0]+=1
    n_list[-1]-=1
    n_list.sort()

print(n_list[-1]-n_list[0])