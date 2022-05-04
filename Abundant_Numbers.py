n=int(input())
tot=0
is_abundant=0
for i in range(1,n):
    if(n%i==0):
        tot=tot+i
    if(tot>n):
        is_abundant=1
        break
if((tot>n) or (is_abundant==1)):
    print(True)
else:
    print(False)