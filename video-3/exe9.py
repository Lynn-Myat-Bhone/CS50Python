def check(a):
    for i in a:
        if len(a)==8 and a.count(a[4])==3:
            return True
        else:
            return False

a = [12,12,19,19,19,3,5,6]
print(check(a))            
        
             
            