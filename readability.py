from cs50 import get_string
letters=sentences=words=0
text=get_string("Text: ")

for i in range(len(text)):
    
    if text[i].isalpha():
        letters += 1
    
    if text[i] == ' ':
        words += 1
        
    if text[i] in ['?','!','.']:
        sentences += 1
        
words += 1;
L,S=((letters/words)*100),((sentences/words)*100)
grade= round(0.0588 * L - 0.296 * S - 15.8)

if grade < 1:
    print("before grade 1")
elif grade > 16:
    print("Grade 16+")
else:
    print(f"grade  {grade}")