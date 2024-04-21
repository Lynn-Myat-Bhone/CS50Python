x = input("Enter a string: ")
# u = ''.join(reversed(x)) # reverse method
u = x[::-1]
print(u)
if u==x:
    print("Yes It is palindrome")
else :
    print("It's not palindrome")
