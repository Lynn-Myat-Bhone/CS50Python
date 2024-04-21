with open("student.csv","r") as file:
    for i in file:
        # print(i.strip().split(","))
        # row = i.strip().split(",")
        # print(f"{row[0]} is in {row[1]}")
        
        # amazing techics in python
        name,house = i.strip().split(",")
        print(f"{name} is in {house}")