a=int(input("enter a:"))
choice=int(input("enter choice:"))
b=int(input("enter b:"))
if choice == 1:
    print(a+b)
elif choice == 2:
    print(a-b)
elif choice == 3:
    print(a*b)
elif choice==4:
    print(a/b)
else:
    print("enter valid choice")