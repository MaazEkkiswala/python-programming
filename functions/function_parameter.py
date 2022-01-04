def one():
    a=int(input("enter number of students::"))
    two(a)

def two(a):
    i=1
    while i<=a:
        name=input("enter name:")
        sub=int(input("enter how many sub:"))
        subject(sub)
        i=i+1


def subject(sub):
    j=1
    while j<=sub:
        ma=int(input("enter marks:"))
        j=j+1
one()

