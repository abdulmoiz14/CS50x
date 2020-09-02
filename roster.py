from cs50 import SQL
from sys import argv
if len(argv) > 3:
    print("command line argument error!")
    exit(1)
db = SQL("sqlite:///students.db")
result = db.execute("SELECT * from students where house = '%s' ORDER BY last,first" % argv[-1])
for row in result:
    print(row['first'] + (' ' + row['middle'] + ' ' if row['middle']!= None else ' ') + row['last'] + ', Born ' + str(row['birth']))