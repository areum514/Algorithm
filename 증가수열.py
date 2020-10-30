import sys
from collections import deque
sys.stdin=open("input.txt","r")
n=int(input())
a=list(map(int,input().split()))

lt=0
rt=n-1
last=0
res=""
tmp=[]
while lt<=rt:
    if a[lt]>last:
        tmp.append((a[lt],'L'))
    if a[rt]>last:
        tmp.append((a[rt],'R'))
    tmp.sort()
    if len(tmp)==0:
        break
    else:
        res=res+tmp[0][1]
        last=tmp[0][0]
        if tmp[0][1]=='L':
            lt+=1
        else:
            rt-=1
    tmp.clear()
print(len(res))
print(res)
"""
n_q=deque(a)
a_l=[]
cnt=0

last=0
for i in range(n):
    if len(n_q)==1:
        if n_q[0]>last:
            a_l.append("L")
            cnt+=1
            break
        
    if n_q[0]<last and n_q[-1]<last:
        break

    elif n_q[0]>=last and n_q[-1]<=last:
        last=n_q[0]
        print("L",end="")
        n_q.popleft()
        cnt+=1
    elif n_q[0]<=last and n_q[-1]>=last:
        last=n_q[-1]           
        print("R",end="")
        n_q.pop()
        cnt+=1 
    else :
        if n_q[0]<n_q[-1]:
            last=n_q[0]
            print("L",end="")
            n_q.popleft()
            cnt+=1
        else:
            last=n_q[-1]           
            print("R",end="")
            n_q.pop()
            cnt+=1 
"""