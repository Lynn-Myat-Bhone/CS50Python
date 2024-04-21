def main():
    number = getNum()
    meow(number)

def meow(n):
    for i in range(n):
        print("Meow")
        
def getNum():
    n = int(input("Enter a number : ")) 
    if n<=0:
        print("invalid")
    return n
main()
    