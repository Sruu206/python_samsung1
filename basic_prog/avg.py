score=int(input('Enter avg score of a Student'))
if 0<=score<=49:
    print("Fail")
elif 50<=score<=79:
    print('Second class')
elif 80<=score<=95:
    print('First class')
elif 96<=score<=100:
    print('Distinction')
else:
    print('Invalid Score')