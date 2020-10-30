import sys
#sys.stdin=open("../input.txt","r")
n=int(input())
a=list(map(int,input().split()))

avg=round(sum(a)/n+0.5)

num=0
diff=avg
index=0
for i in range(n):
    if abs(avg-a[i])<=diff:
        if num<a[i]:
            num=a[i]
            index=i
            diff=abs(avg-a[i])

print(avg,end=" ")
print(index)

