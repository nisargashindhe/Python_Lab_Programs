#10. Implement Stack

stack=[]
stack_size=int(input(" Enter the size of a STACK : "))

def push_item(item):
    if(len(stack)<stack_size):
        stack.append(item)
        print(f'{item} is inserted::')
    else :
        print(f'Stack is full::')

def pop_item():
    if(len(stack)>0):
       print(f'Item removed::{stack.pop()}')
    else:
       print('Stack is empty::')

def display():
    if(len(stack)>0):
       print('Elemets of stack are::')
       for i in stack:
          print(i)
    else:
       print('Stack is Empty::')

def main():
    while True :
       ch=int(input('Enter your choice:\n1.Push\n2.Pop\n3.Display\n4.Exit\n'))

       if ch==1:
            num=int(input('Enter the element to be pushed::'))
            push_item(num)
       elif ch==2:
            pop_item()
       elif ch==3:
            display()
       elif ch==4:
            break
       else:
            print('Invalid Choice::')

if __name__=="__main__":
 main()