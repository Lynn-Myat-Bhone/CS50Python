def main():
    x = int(input("Enter a number: "))
    if check(x):
        print("Even")
    else:
        print("Odd")

def check(n):
    if n%2==0:
        return True
    else:
        return False

main()