l = []
for x in range(10):
    l.append(int(input('enter a no:')))
even = 0
odd = 0

for y in range(10):
    if l[y]%2 == 0:
        even += 1
    else:
        odd += 1


print("in the entered no's","\nno of odd's are",odd,"\nno of even's are",even)