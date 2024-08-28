num=int(input("Enter the number of rows: "))
for i in range(num):
    for j in range(num):
        if j<=i:
            print(j,end=" ")
        else:
            print(" ",end="")
    print()

# num2=int(input("Enter the number of rows: "))
# for i in range(num2):
#     for j in range(num2):
#         if j<=i:
#             print(i,end="")
#         else:
#             print(" ",end="")
#     print()