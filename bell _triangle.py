# bell numbers = 1 1 2 5 15 52 203 877 4140 ....
num=int(input("Enter the number of rows: "))
l1=[1] # for first row since it only contain 1
l2=[] 
for i in range(num):
    l2.append(l1[-1])  # since in the current row the first element is the last element of the previous row i.e, l1
    for j in l1:
        l2.append(j+l2[-1])  # add the corresponding elements of the previous and current row
    
    print(l1)
    l1=list(l2)
    l2.clear()