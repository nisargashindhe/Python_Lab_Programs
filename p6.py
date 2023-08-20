#6. Implement a sequential search

def getkey():
        num=int(input(" Enter the element to be Searched : "))
        return num
def sequential_search(elements,key):
        found=False
        for i in range(len(elements)):
                if(key==elements[i]):
                        found=True
                        break
        if(found==True):
               print(f' The {key} Element is present at the position : {i+1} ')
        else:
               print(f' The {key} Element Does not Found !!!')

def main():
        elements=[]
        size=int(input("Enter the size of an List : "))
        print(" Enter the elements : ")
        for i in range(size):
                i=int(input())
                elements.append(i)
        key=getkey()
        sequential_search(elements,key)

if __name__=="__main__":
    main()