a=int(input("enter number a:"))
b=int(input("enter number b:"))
c=int(input("enter number c:"))
gst1=int(input("Enter gst"))
total= a+b+c
gst=(total*gst1)/100
Ans=total+gst
print(total)
print(gst)
print(Ans)
# c=input("enter + for add * for mul - for sub and /:")
# if c == '+':
#     print("your addition is:",a+b)
# elif c == '*':
#     print(a*b)
# elif c == '-':
#     print(a-b)
# elif c == '/':
#     print(a/b)
# else:
#     print("enter valid input")
