l = []
for x in range(10):
    l.append(int(input('enter a no:')))

l.sort()
print(l)
print('biggest is ',l[-1])
print('second biggest is ',l[-2])