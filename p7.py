#7. Create a calculator program.

def add(a,b):
    return (a+b)

def sub(a,b):
    return (a-b)

def multi(a,b):
    return (a*b)

def div(a,b):
    return (a/b)

def fdiv(a,b):
    return (a//b)

while(True):
        print(" \n------- Enter Your Choice ------- ")
        print(" 1.Addition\n 2.Substraction\n 3.Multiplication\n 4.Division\n5.Floor Division\n ")
        ch = int(input(" Enter Here --> "))

        if(ch==1):
             num1=int(input(" Enter 1st Number : "))
             num2=int(input(" Enter 2nd Number : "))
             print(f'The Sum of {num1} and {num2} is {add(num1,num2)}')
        elif(ch==2):
             num1=int(input(" Enter 1st Number : "))
             num2=int(input(" Enter 2nd Number : "))
             print(f'The Substraction of {num1} and {num2} is {sub(num1,num2)}')
        elif(ch==3):
             num1=int(input(" Enter 1st Number : "))
             num2=int(input(" Enter 2nd Number : "))
             print(f'The product of {num1} and {num2} is {multi(num1,num2)}')
        elif(ch==4):
             num1=int(input(" Enter 1st Number : "))
             num2=int(input(" Enter 2nd Number : "))
             print(f'The Quotient of {num1} and {num2} is {div(num1,num2)}')
        elif(ch==5):
             num1=int(input(" Enter 1st Number : "))
             num2=int(input(" Enter 2nd Number : "))
             print(f'The Floor Division of {num1} and {num2} is {fdiv(num1,num2)}')
        else:
             print(" Enter a valid Choice ")
             print(" \n Do you want to continue ..? ")
             val = input(" Yes or No : ")
             if(val=="no"):
                  break
