def formula(n):
    sum =0
    for i in range(1,n):
        sum = 1/i + sum
    return sum
def main():
    x = int(input("How many num do u wanna sum? :"))
    print("Answer is ",formula(x))


if __name__=="__main__":
    main()