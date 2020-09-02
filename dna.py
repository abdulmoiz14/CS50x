from sys import argv
import csv

# check command line argument 
if len(argv) > 3:
    print("command argument error")
    exit(1)
    
# open files
csvfile = open(argv[1],"r")
txtfile = open(argv[2],"r").read()

# read data from csv file
STR = []
persons = {}
for index,row in enumerate(csvfile):
    
    if index == 0:
        STR = [strand for strand in row.strip().split(',')][1:]
        
    else:
        curr_row=row.strip().split(',')
        persons[curr_row[0]] = [int(x) for x in curr_row[1:]]
   
# read dna from text file
dna = []
for strand in STR:
    
    i=0
    max_str =- 1
    count = 0
    
    while i < len(txtfile):
        
        temp = txtfile[i:i+len(strand)]
        
        if strand == temp:
            count += 1
            max_str = max(max_str,count)
            i += len(strand)
        
        else:
            i += 1
            count = 0
    dna.append(max_str)

# checking for a match    
notfound = 0
for name,STRs in persons.items():
    if STRs == dna:
        print(name)
        notfound = 1
        
if notfound != 1:
    print("No match")