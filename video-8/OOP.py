class Student:
    def __init__(self,name,house): #like constructor
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor","huffepuff","Ravenclaw","Slytherin"]:
            raise ValueError("Missing house")
        self.name= name # self is this 
        self.house = house 
        
        
    def __str__(self):
        return f"{self.name} from {self.house}"
    @classmethod
    def get(cls):
        name = input("Name : ")
        house = input("House : ")
        student = Student(name,house)
        return cls(name,house)

def main():
    
    print( Student.get())


if __name__=="__main__":
    main()