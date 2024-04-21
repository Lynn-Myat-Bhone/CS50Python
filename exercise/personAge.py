from datetime import date
class Person:
    def __init__(self,name,country,DOB):
        self.name= name
        self.country = country
        self.DOB = DOB
    
    def calculate_age(self):
        today = date.today()
        if self.DOB.year>today.year:
            print("Invalid DOB")
        else:
            age = today.year-self.DOB.year
        return age
    
person = Person("Lynn Myat Bhone","Myanmar",date(2004,12,31)) # year- month - day
print("Name :", person.name)
print("Country : ",person.country)
print("DOB: ",person.DOB)
print("Age : ",person.calculate_age())