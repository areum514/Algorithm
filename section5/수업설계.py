import sys
from collections import deque
sys.stdin=open("../input.txt", "r")
need=input()
n=int(input())
for i in range(n):
    plan=input()
    dq=deque(need)
    for x in plan:
        if x in dq:
            if x!=dq.popleft():
                print("#%d NO" %(i+1))
                break
    else:
        if len(dq)==0:
            print("#%d YES" %(i+1))
        else:
            print("#%d NO" %(i+1))

""" import sys
from collections import deque

sys.stdin=open("../input.txt","r")
need=deque(input())
n=int(input())

for i in range(n):
    plan=deque(input())
    dq=deque(need)
    
    while dq and plan: 
        if plan.popleft()==dq[0]:
            dq.popleft()
    if dq:
        print("#%d N0"%(i+1))
    else: 
        print("#%d YES"%(i+1))

 """