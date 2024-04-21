x = [10,11,12,13,10]
length= len(x)
for i in x:
    if x[0]==x[length-1]:
        result = True
    else:
        result= False
print(result)


y = [10,11,12,13,20]
length = len(y)
for i in y:
    if y[0]==y[length-1]:
        result = True
    else:
        result = False
print(result)