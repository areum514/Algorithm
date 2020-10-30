import sys
sys.stdin=open("input.txt","r")
n=int(input())
n_list=list(map(int,input().split()))
print(n_list)
answer_list=[0]*n
cnt=0
for i in range(n):
    for j in range(n_list.index(i+1)):
        if n_list[j]>i:
            cnt+=1
    answer_list[i]=cnt
    cnt=0
print(answer_list)