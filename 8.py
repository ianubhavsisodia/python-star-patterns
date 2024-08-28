for i in range(4):
    for j in range(4):
        if j<=i:
            print("{}".format(j+1,),end="")
        else:
            print(" ",end="")
    print()
    