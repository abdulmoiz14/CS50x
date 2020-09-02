from cs50 import get_int

height = get_int("height: ")

while height < 1 or height > 8:
    height = get_int("height: ")
    

for i in range(height):
    
    for space in range(height - i - 1):
        print(" ", end="")
        
    for j in range(i + 1):
        print("#", end="")
        
    print("  ", end="")
    
    for k in range(i+1):
        print("#", end="")
        
    print("")
