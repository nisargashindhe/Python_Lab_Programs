#4. Display Multiplication Tables

n=int(input(" Enter a number : "))
i=1
print(f" The Multiplication Table of {n} :: ")
while (i<=10):
   print(f'{n} * {i} = {n*i}')
   i += 1