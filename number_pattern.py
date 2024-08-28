a=int(input("Enter the number of rows: "))
for i in range(a):
    for j in range(a-i):
        print("{}".format(j+1),end=" ")
        print(" ",end="")
    print()


for i in range(a):
    for j in range(a-i):
        print("{}".format(a-i),end="")
        print(" ", end=" ")
    print()
