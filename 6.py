for i in range(4):
    for j in range(7):
        if  i<=j<=6-i:
            print("*",end="")
        else:
            print(" ",end="")
    print()