import sys
from collections import deque

sys.stdin=open("../input.txt","r")
n,k=map(int,input().split())
a=list(x for x in range(1,n+1))
d=deque(a)
cnt=0
pt=0

while d:
    for _ in range(k-1):
        d.append(d.popleft())
    d.popleft()
    if len(d)==1:
        break
            
print(d[0])