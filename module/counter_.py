from collections import Counter
   
# With sequence of items 
print(Counter(['B','B','A','B','C','A','B','B','A','C']))
   
# with dictionary
count = Counter({'A':3, 'B':5, 'C':2})
print(count)
 
count.update(['A', 2])
print(count)