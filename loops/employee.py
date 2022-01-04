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
print(income)



