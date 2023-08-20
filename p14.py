#7. Demonstrate Exceptions in Python

try :
    num=int(input("Enter a number::"))
    print(num)
except ValueError:
    print('Enter a numeric value::')
finally :
    print('Always Executes:::')
