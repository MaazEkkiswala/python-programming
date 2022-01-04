a=['hello',4,5,6,'how','are','you',4,5,67,8]
s=[]
n=[]
for i in a:
    if type(i) == str:
        s.append(i)
    else:
        n.append(i)
print(s)
print(n)
