import math
def main():
    x = int (input("Enter a number: "))
    print("The square of ",x," is ",calculate(x))
    
def calculate(n):
    return n * n

if __name__ == "__main__":
    main()