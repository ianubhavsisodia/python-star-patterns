a=int(input("Enter the number of rows: "))
for i in range(a):
    for j in range(a):
        if j==0 or (i==a-1) or j==i:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

