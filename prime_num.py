# prime number = natural number greater than 1 that has ni positive divisors other than 1 and itself
a=int(input("Enter the range: "))
for i in range(a):
    if i>1:
        for j in range (2,i):
            if (i%j)==0:
                break
        else:
            print(i) 
    

# check prime number
# num=int(input("Enter the number to check: "))

# for i in range(2,num):
#     if num%i==0:
#         print("not prime")
#         break
# else:
#     print("Prime number")