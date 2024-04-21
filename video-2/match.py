name=input("What's your name: ")
match name :
    case "Harry" | "Hermione" | "Ron": # or statement
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:# default
        print("Who r u?")