import random
otp=random.randrange(100000,1000000)
print(otp)
user=int(input("enter the six digit otp :"))
if otp==user:
    print('HURRAH')
    print('you logged in successfully')
else:
    print('you entered the wrong otp')
