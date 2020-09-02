from cs50 import get_int

height = get_int("height = ")

while height < 1:
    height = get_int("height = ")
    
for i in range(height):
    
    for k in range(i+1):
        print("#",end="")
        
    print("")
