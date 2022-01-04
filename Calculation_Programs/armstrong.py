# num=int(input("Enter any positive number==>"))
# x=num%10
# print(x)
num=int(input("Enter any positive number==>"))
sum=0
temp=num
while temp > 0 :
    digit=temp % 10
    sum+=digit**3
    temp//=10

if sum==num:
    print(num,"Armstrong number")
else:
    print(num,"Not Armstrong number")
