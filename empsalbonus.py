name=input('enter name:')
sal=float(input('enter salary:'))
des=input('enter des is m/a/c:')
if des=='m' or des=='M':
    bon= sal*0.2
elif des=='a' or des=='A':
    bon=sal*0.1
else:
    if des=='c' or des=='C':
        bon=sal*0.05
    else:
        print('invalid des')
print('total salary is:',sal+bon)
