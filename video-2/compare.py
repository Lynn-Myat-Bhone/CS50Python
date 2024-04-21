y = int(input("What your number: "))
x = 10
if y<x:
    print(y,"is less than ",x)
     
elif x==y:
    print(y,"is equal ",x)
    
elif 20<y<30:# you can write "and" statement like this
    print(y ,"is between 20 and 30")
else:
    print(y,"is greater than",x)