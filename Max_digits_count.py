n=int(input())
k=list(map(int,input().split()))
e=[]
for i in k:
    s=str(i)
    k=len(s)
    e.append(k)
l=max(e)
c=0
for i in e:
    if i==l:
        c+=1
print(c)