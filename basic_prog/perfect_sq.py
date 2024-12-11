import math
num=int(input("Enter a number"))
n= math.sqrt(num)
print(type(n))
n=math.floor(num)
print(type(n))
if n*n ==num:
    print(num,"is Perfect square")
else:
    print(num,"is not a Perfect square")
