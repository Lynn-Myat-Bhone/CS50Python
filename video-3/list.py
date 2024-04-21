student =["Ron","DoDo","Lynn",1] # list - store mutltiplae items in single value
student1 = ("Draco","Elena",200) # tuples - ordered and unchangeable 
student2 ={"fork","spoon","Dog",40} # sets - unordered and unindexed. No duplicate value

for i in student:
    print(i)
    
for i in range(len(student)):# range only accepted int 
    print(i+1, student[i])