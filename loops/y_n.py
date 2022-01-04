x1=['y','y','n','y','n',None,'','y','n']
count=0
count1=0
total=0
x=0
for i in x1:
    count=count+1
    if i == 'y':
        count1=count1+1
        print(count,"y")
    elif i=='n':
        print(count,"n")
        total=total+1
    else:
        pass
print("total number of y",count1,)
print("total number of n",total)
# for j in range(len(x1)):
#     total=total+1
#     if i == 'y':
#     #   total=total+x
#         print(total)

