k=2
for i in range(4):
    for j in range(7):
        if i+j==3 or j-i==3:
            print("*",end=" ")
        elif i==3 and j!=k: 
            print("*",end=" ")
        else:
            print(" ",end="")
    print()