import random
import string 
len_gth=random.randint(10,14)
low_letters=string.ascii_lowercase
print(low_letters)
uper_letters=string.ascii_uppercase
digits=string.digits
pun=(string.punctuation)
ls=list(low_letters+uper_letters+digits+pun)
otp=random.choices(ls,k=len_gth-2)

print('your password is--> ', *otp,sep='')
print()
print('---------------------')
    



