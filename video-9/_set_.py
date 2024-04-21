students = [{"name ": "Harry","house":"Gryffindor"},
           {"name ": "Ron","house":"Gryffindor"},
           {"name ": "Draco","house":"Slytherin"},
           {"name ": "Panda","house":"Ravenclaw",}]

houses = set()
for student in students:
   houses.add(student["house"]) 

print(sorted(houses))