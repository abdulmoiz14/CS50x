from cs50 import get_int

rows = get_int("height: ")

while height < 1 and height > 8:
    rows = get_int("height: ")
    
for i in range(rows):
    
    for space in range(rows - i):
        print(" ",end = "")
        
    for j in range(i + 1):
        print("#",end = "")
        
    print("  ",end = "")
    
    for k in range(i+1):
        print("#",end="")
        
    print("")