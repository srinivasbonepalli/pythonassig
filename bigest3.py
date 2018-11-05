a=int(input('enter a no:'))
b=int(input('enter a no:'))
c=int(input('enter a no:'))
if a>b and a>c:
    print(a,' is greatest')
elif b>a and b>c:
    print(b,' is greatest')
elif a==b and b==c:
    print('all are equal')
else:
    print(c,' is greatest')
