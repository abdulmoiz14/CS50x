from cs50 import get_float
change = get_float("changed owe : ")
while change < 0 :
    change = get_float("changed owe : ")
cents=round(change*100)
quarter,dime,nickel,penny = 25,10,5,1
q=d=n=p=0
while(cents!=0):
    if cents >= quarter:
        cents -= quarter
        q+=1
    elif cents < quarter and cents >= dime:
        cents -= dime
        d+=1
    elif cents < dime and cents >= nickel:
        cents -= nickel
        n+=1
    elif cents < nickel and cents >= penny:
        cents -= penny
        p+=1
total = q+d+n+p
print(total)