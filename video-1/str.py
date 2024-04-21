name =input("Your name: ")

""""name=name.strip()#remove space from in front and back
name=name.title()#capitilize letters afterr space(Lynn Myat)
name = name.capitalize()#capitilize first letter

name = input("Your name:").strip().title() #the short way to write above method"""

print("hello, "+name, end="\n")
print("Welcome")
first,last = name.split(" ")# name splitting
print(f"hello, {first}")#new method



