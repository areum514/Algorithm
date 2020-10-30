import sys
from collections import deque
#sys.stdin=open("input.txt","r")
n=int(input())
n_l=list(map(int,input().split()))
n_q=deque(n_l)
a_l=[]
cnt=0

largest=0
for i in range(n):
    if len(n_q)==1:
        if n_q[0]>largest:
            a_l.append("L")
            cnt+=1
            break
        
    if n_q[0]<largest and n_q[-1]<largest:
        break

    elif n_q[0]>=largest and n_q[-1]<=largest:
        largest=n_q[0]
        print("L",end="")
        n_q.popleft()
        cnt+=1
    elif n_q[0]<=largest and n_q[-1]>=largest:
        largest=n_q[-1]           
        print("R",end="")
        n_q.pop()
        cnt+=1 
    else :
        if n_q[0]<n_q[-1]:
            largest=n_q[0]
            print("L",end="")
            n_q.popleft()
            cnt+=1
        else:
            largest=n_q[-1]           
            print("R",end="")
            n_q.pop()
            cnt+=1 
