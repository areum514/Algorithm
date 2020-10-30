"""5 140
90 50 70 100 60"""
import sys
from collections import deque
"""list는 팝할때 계속 이동하니 deque 이용"""
sys.stdin=open("input.txt","r")
n,m=map(int,input().split())
p_list=list(map(int,input().split()))
p_list.sort()
p=deque(p_list)
cnt=0

while p:
    if p[0]+p[-1]<=m:
        p.popleft()
    cnt+=1
    p.pop()
    if len(p)==1:
        cnt+=1
        break
print(cnt)


