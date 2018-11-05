name=input('enter your name:')
slab=input('enter slab type(industry(i/I)/commercial(c/C)/residential(r/R):')
if slab=='i' or slab=='c' or slab=='r'or slab=='I'or slab=='C' or slab=='R':
    units = int(input("enter no of units used:"))
    print('Generating the bill')
    if slab=='i' or slab=='I':
        bill=units*5.25
        print(name,'',bill,' is your industry bill')
    elif slab=='c' or slab=='C':
        bill=units*4.00
        print(name,'',bill, ' is your commercial bill')
    else :
        bill=units*3.08
        print(name,'',bill, ' is your residency bill')
else:
    print('invalid input')
