# with open("name.txt","r")as file: # r is read
#     lines= file.readlines()
# for i in lines:
#     print(i.strip())
    
# with open ("name.txt","r") as file: # simple version 
#     for i in file:
#         print(i.strip())
       
 
name = []
with open ("name.txt","r") as file:
    for i in file:
        name.append(i.strip())
for name in sorted(name):  #sorted(name) is ascending, sorted(name,reverse=True) is decending
    print(f"hello,{name}")