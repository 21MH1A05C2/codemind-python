Num = int(input())
length = len(str(Num))

Temp = Num
S = 0
rem = 0

while Temp > 0:
    rem = Temp % 10
    S = S + (rem**length)
    Temp = Temp // 10
    length = length - 1

if S == Num:
    print("True")
else:
    print("False")