def odd_even():
    i=int(input("enter number:"))
    if i %2 ==0:
        s="even"
    else:
        s="odd"
    return s



def prime():
    a=int(input("enter number to check if it is prime or not=="))
    if a==2 or a==3 or a==5 or a==7:
        s=("prime")
    elif a%2==0 or a%3==0 or a%5==0 or a%7==0:
        s=("not prime")
    else:
        s=("prime")

    return s



def factorial():
    n=int(input("Enter number==>"))
    result=1
    for i in range(n,0,-1):
        result=result*i
    s=result
    return s

def match():
    n=int(input("How many team="))
    team=[]
    for i in range(n):
        name=input("Enter team name=")
        win=int(input("how many match won="))
        if win>2 and win<5:
            print("qualified")
            team.append(name)
        else:
            print("Not qualified")
    return team

def palindrome():
    s= input("Enter any number")
    reverse=s[::-1]
    if(s==reverse):
        print("palindrome")
    else:
        print("Not palindrome")
    return s

def gst():
    a=int(input("enter number a:"))
    b=int(input("enter number b:"))
    c=int(input("enter number c:"))
    gst1=int(input("Enter gst"))
    total= a+b+c
    gst=(total*gst1)/100
    Ans=total+gst
    print(total)
    print(gst)
    return Ans

def employee():
    n=int(input("How many employees"))
    income=[]
    salary=0
    increement=int(input("how much increement (%) ="))

    for i in range (n):
        name=input("enter name=")
        desig=input("enter designation=")
        salary=int(input("enter salary="))
        per=salary*increement/100
        salary1=salary+per
        income.append(salary1)
    return income

def tell_index():
    a=['a','b','c','d']
    a1=int(input("which index-"))
    return a[a1]

def armstromg():
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
    return num
def calculator():
    a=int(input("enter a:"))
    choice=int(input("enter choice:"))
    b=int(input("enter b:"))
    if choice == 1:
        s=print(a+b)
    elif choice == 2:
        s=print(a-b)
    elif choice == 3:
        s=print(a*b)
    elif choice==4:
        s=print(a/b)
    else:
        print("enter valid choice")
    return s


while True:
    choice=int(input("enter choice"))
    if choice==1:
        o=odd_even()
        print(o)
    elif choice==2:
        p=prime()
        print(p)
    elif choice==3:
        f=factorial()
        print(f)
    elif choice==4:
        m=match()
        print(m)
    elif choice==5:
        p=palindrome()
        print(p)
    elif choice==6:
        g=gst()
        print(g)
    elif choice==7:
        e=employee()
        print(e)
    elif choice==8:
        i=tell_index()
        print(i)
    elif choice==9:
        a=armstromg()
        print(a)
    elif choice==10:
        c=calculator()
        print(c)
    elif choice==0:
        break
    else:
        print("enter valid number ranging from 1 to 10")


