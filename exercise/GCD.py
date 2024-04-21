import math
def GCD(a,b):
    return math.gcd(a,b)
def main():
    x= int(input("Enter a number : "))
    y = int(input("Entera number 2 :"))
    print("The greatest common divisor is ", GCD(x,y))

main()