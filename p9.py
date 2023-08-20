#9. Implement Selection Sort

def selectionSort(elements,size):
  for step in range(size):
    min_idx = step
    for i in range(step + 1, size):
      # to sort in descending order, change > to < in this line
      if elements[i] < elements[min_idx]:
        min_idx = i
      # put min at the correct position
        (elements[step], elements[min_idx]) = (elements[min_idx], elements[step])

def main():
 elements=[]
 size=int(input("Enter the size of an List : "))
 print(" Enter the elements : ")
 for i in range(size):
   i=int(input())
   elements.append(i)
 size=len(elements)
 selectionSort(elements,size)
 print('Sorted Array in Ascending Order:')
 print(elements)

if __name__=="__main__":
 main()
