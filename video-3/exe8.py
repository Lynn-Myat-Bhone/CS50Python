
def check(num):
    count12 = 0
    count9 = 0
    for i in a:
        if i == 12:
            count12+=1
        if i == 9 :
            count9 +=1

    if count12==2 and count9 ==3:
        return True
    else:
        return False
    

a = [12,12,9,9,9,3,5]
print(check(a))
