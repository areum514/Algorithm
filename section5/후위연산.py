import sys
from collections import deque

sys.stdin=open("../input.txt","r")
a=input()
stack=[]

for x in a:
    if x.isdecimal():
        stack.append(int(x))
    else:
        b=stack.pop()
        a=stack.pop()
        if x=="+":
            stack.append(a+b)
        elif x=="-":
            stack.append(a-b)
        elif x=="*":
            stack.append(a*b)
        elif x=="/": 
            stack.append(a/b)
print(stack.pop())
""" d=deque()


for x in a:
    if x.isdecimal():
        d.append(x)
    else: 
        b=int(d.pop())
        a=int(d.pop())
        if x=="+":
            d.append(a+b)
        elif x=="-":
            d.append(a-b)
        elif x=="*":
            d.append(a*b)
        else: 
            d.append(a/b)

        
print(d[0])

 """



