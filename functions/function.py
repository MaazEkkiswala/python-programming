#a=[2,3,4,5,6,7,8,9]
e=[]
o=[]

for i in range(1,10):
    if i %2 ==0:
        e.append(i)
        #print("even")
    else:
        o.append(i)
        #print("odd")
print(e)
print(o)