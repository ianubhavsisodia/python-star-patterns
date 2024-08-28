# factorial = factorial of a non-negative integer n,denoted by n!,
# is the product of all positive integers less than or equal to n. For example: 5! = 120

#factorial using inbuilt func
import math
num=int(input("Enter the number: "))
result=math.factorial(num)
print(result)

#factorial using recursion
def fact(n):
    if (n==0):
        return 1
    else:
        return n*fact(n-1)

num=int(input("Enter the number: "))
print(fact(num))

# using loop
num= int(input("Enter the number: "))
if num==0:
    print(1)
else:
    result = 1
    for i in range(num,0,-1):
        result= result*i
    print(result)