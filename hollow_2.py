
for i in range(4):
    for j in range(7):
        if i==3 or i+j==3 or j-i==3:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()