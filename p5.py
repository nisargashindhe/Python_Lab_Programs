#5. Check if a given number is a Prime Number or not

n=int(input(" Enter a Number to check Number Wheather it is Prime or Not : "))
flag=False
if(n==1):
        print(f'{n} is not a Prime Number')
else:
        for i in range(2,n):
               if(n%i==0):
                flag=True
                break
        if(flag==False):
              print(f'{n} is a prime number')
        else:
              print(f'{n} is not a prime number')