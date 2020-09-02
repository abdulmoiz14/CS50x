from cs50 import get_string
import sys
credit=get_string("number : ")
credit_copy = credit[::-1]

if len(credit) in (13,15,16):
    answar = sum( [ (int(x) * 2) // 10 + ((int(x) * 2) % 10) for x in credit_copy[1::2] ]) + sum([int(x) for x in credit_copy[0::2]])
else:
    print("INVALID")
    exit()
    
if (answar % 10) == 0:
    if (int(credit[0]) == 4) and len(credit) in (13,16):
        print("VISA")
    elif (51 <= int(credit[0:2]) <= 55) and len(credit) == 16:
        print("MASTERCARD")
    elif (int(credit[0:2]) in (34,37)) and len(credit) == 15:
        print("AMEX")
else:
    print("INVALID")