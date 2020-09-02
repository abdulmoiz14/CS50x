from sys import argv
from cs50 import SQL
import csv
if len(argv) > 3:
    print("command line argument error!")
    exit(1)
db = SQL("sqlite:///students.db")
with open(argv[-1],"r") as file:
    reader =  csv.DictReader(file)
    for row in reader:
        full_name = row['name'].split()
        if len(full_name) == 3:
            first,middle,last=full_name
        else:
            first,last=full_name
            middle = None
        house = row["house"]
        birth = row["birth"]
        db.execute("INSERT INTO students (first, middle,last,house,birth) VALUES(?, ?, ?,?,?)",first,middle,last,house,birth)