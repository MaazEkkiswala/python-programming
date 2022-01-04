def number():
    a=int(input("enter number of students::"))
    name(a)
    return a

def name(a):
    i=1
    n=[]
    while i<=a:
        name=input("enter name:")
        n.append(name)
        sub=int(input("enter how many sub:"))
        subject(sub)
        i=i+1
    return n

def subject(sub):
    j=1
    t=0
    total=[]
    while j<=sub:
        ma=int(input("enter marks:"))
        t=t+ma
        total.append(t)
        j=j+1
    print(total)
        
        
        


number()



# mark=[]
# name1=[]
# for i in range(n):
#     name=input("enter name:")
#     name1.append(name)
#     sub=int(input("how many subjects:"))
#     total=0
#     for j in range(sub):
#         marks=int(input("enter marks:"))
#         total=total+marks  
        
#     print(total)
#     mark.append(total)
# z=dict(zip(name1,mark))
# print(z)
# print(mark)
# print(name1)        


