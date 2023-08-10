#import libraries
import random
import string

#length of the password
length=int(input("enter required length of the password:"))

#assign numbers,characters,letters,,etc....
letters=string.ascii_letters
nums=string.digits
chars=letters+nums+"!@#$%*"

rnd=random.SystemRandom()

print("your password:")
print(''.join(rnd.choice(chars) for i in range(length)))

