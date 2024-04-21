name = input("Enter a name: ")

file = open("name.txt","a")# a= append, w = write but recreate file 
file.write(f"{name}\n")
file.close()

# with open("name.txt","a") as file: # the same as above but dont need to write close()
#     file.write(f"{name}\n")