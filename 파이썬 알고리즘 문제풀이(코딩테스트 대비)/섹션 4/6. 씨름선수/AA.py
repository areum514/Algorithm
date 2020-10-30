import sys

#sys.stdin=open("input.txt","r")
n=int(input())
body=[]
largest=0
cnt=0
for i in range(n):
    a,b=map(int,input().split())
    body.append((a,b))
body.sort(reverse=True)

for a,b in body:
    if b>largest:
        largest=b
        cnt+=1
print(cnt)