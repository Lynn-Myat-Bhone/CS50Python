# while True:
#     try:
#         x = int(input("Number: "))
#     except ValueError:
#         print("x is not an integer")
#     else:
#         break
# print(f"x is {x}")

while True:
    try:
        x = int(input("Number: "))
    except ValueError:
        pass # dont wanna anything just pass
    else:
        break
print(f"x is {x}")