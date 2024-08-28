for i in range(5):
    for j in range(5):
        if j<=4-i:
            print("{}".format((5-(j+i))),end="")
        else:
            print(" ", end='')
    print()


# for i in range(5):
#k=5-i
#     for j in range(5):
#         if j<=4-i:
#             print(k,end="")
#         k-=1
#         else:
#             print(" ", end='')
#     print()