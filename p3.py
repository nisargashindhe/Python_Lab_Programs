#3. Find the sum of n natural numbers

num=int(input(" Enter a Number : "))
i=1
sum=0
if(num<0):
   print(" Enter a positive number ")
else:
  while(i<=num):
    sum += i
    i += 1
print(f'The Sum of first {num} natural numbers is {sum} ')