n=input()
n=n.lower()
v=list("aeiou")
c=0
for i in n:
    if i in v:
        v.remove(i)
if len(v)==0:
    print("0")
else:
    print(*v)