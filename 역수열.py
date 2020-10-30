import sys
sys.stdin=open("input.txt","r")
n=int(input())
a=list(map(int,input().split()))
seq=[0]*n
cnt=0


for i in range(n):
    for j in range(n):
        if a[i]==0 and seq[j]==0:
            seq[j]=i+1
            break
        elif seq[j]==0:
            a[i]-=1
print(seq)

""" for i in range(n):
    for j in range(n):
        if a[i]==0 and seq[j]==0:
            seq[j]=i+1
            break
        elif seq[j]==0:
            a[i]-=1
print(seq)
         """

"""
if answer_list[cnt]==0:
                answer_list[cnt]=i
                break    
            while answer_list[cnt]==0:
                cnt+=1
                print(cnt)
            answer_list[cnt]=i"""