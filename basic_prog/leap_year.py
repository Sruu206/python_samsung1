n=int(input('Enter a year'))
c=(n%4==0 and n%100!=0 or n%400==0)
if(c==True):
    print(n,"is a Leap year")
else:
    print("not a Leap year")