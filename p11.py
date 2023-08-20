#11. Read and write into a file.

#Reading
with open("test.txt","r") as f1:
    c=f1.read()
    print(c)
#Writing
with open("test1.txt","w") as f2:
    f2.write("KLE JT BCA GADAG!!!!!")
    print('Data Written!!!')
