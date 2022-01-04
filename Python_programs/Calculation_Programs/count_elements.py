MyList = ["b", "a", "a", "c", "b","b", "a", "c",'a']
count=0
b=0
count1=[]
for i in MyList:
    if i == 'a': 
        count = count + 1
        count1.append(count) 
    elif i=='b':
        count = count + 1 
        count1.append(count)
print (count1)
