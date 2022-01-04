n=int(input("enter no. of stu:"))

mark=[]
name1=[]
for i in range(n):
    name=input("enter name:")
    name1.append(name)
    sub=int(input("how many subjects:"))
    total=0
    for j in range(sub):
        marks=int(input("enter marks:"))
        total=total+marks  
        
    print(total)
    mark.append(total)
z=dict(zip(name1,mark))
print(z)
# print(mark)
# print(name1)        


