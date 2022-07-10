n=int(input())
a=list(map(int,input().split()))
k=int(input())
sum=0
for i in a:
    if i>k:
        break
    else:
        sum=sum+i
print(sum)