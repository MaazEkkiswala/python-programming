a=int(input("enter number:"))
b=int(input("enter number:"))
c=input("enter + for add * for mul - for sub and /:")
if c == '+':
    print("your addition is:",a+b)
elif c == '*':
    print(a*b)
elif c == '-':
    print(a-b)
elif c == '/':
    print(a/b)
else:
    print("enter valid input")
