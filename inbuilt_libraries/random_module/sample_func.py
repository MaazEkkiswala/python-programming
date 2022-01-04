import random 
a='1234567890'
while True:
    c=int(input("enter length:"))
    print("".join(random.sample(a,c)))