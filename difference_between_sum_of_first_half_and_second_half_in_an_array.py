n=int(input())
a=list(map(int,input().split()))
sum=0
sum1=0
h1=len(a)//2
for i in range(len(a)):
    if i<h1:
        sum=sum+a[i]
for i in range(h1,n):
    sum1=sum1+a[i]
if sum1>sum:
    print(sum1-sum)
else:
    print(sum-sum1)