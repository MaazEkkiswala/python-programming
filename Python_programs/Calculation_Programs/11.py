grocery=10
electronic=20
furniture=30

total=0
a=input("enter category:")
if a=='grocery':
   a1=int(input("how many products = "))
   for i in range(a1):
       p=int(input("price ="))
       total=total+p
       gst=(total*grocery)/100
       total1=total+gst
   print(f"total is:{total},total with gst is:{total1}")
elif a=='electronic':
    a1=int(input("how many products = "))
    
    for i in range(a1):
       p=int(input("price ="))
   
       total=total+p
       gst=(total*electronic)/100
       total1=total+gst
    print(total)
    print(total1)
elif a=='furniture':
    a1=int(input("how many products = "))
   
    for i in range(a1):
       p=int(input("price ="))
      
       total=total+p
    gst=(total*electronic)/100
    total1=total+gst  
    print(total)
    print(total1)
else:
    print("enter valid category")
        

