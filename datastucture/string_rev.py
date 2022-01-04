a=['a','b','c']
b=[]
for i in range(1,len(a)+1):
    print(a[-i])
    b.append(a[-i])
print(b)