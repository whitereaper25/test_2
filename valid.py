import re

def verify(phn_no):
    design =  "[789]\d{9}$"
    if re.match(design,phn_no):
        return "yes"
    else:
        return "No"
n = int(input())
for i in range(n):
    print(verify(input()))