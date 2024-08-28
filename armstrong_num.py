# armstrong num- number of n digits which are equal to sum of nth power of its digits
def isArmStrong(num):
    if len(str(num))==1:
        print('Number is Armstrong')
    elif len(str(num))>1:
        digit=0
        for i in range(len(str(num))):
            digit=digit+(pow(int(str(num)[i]),(len(str(num)))))
            if (digit)==(num):
                print("Number is Armstrong")
                break
        if digit!=num:
            print("NOT ARMSTRONG")


a=int(input("Enter the number: "))
isArmStrong(a)

## code to find armstrong number between 0 to 1000

i=0
while i<1000:
    result=0  # result should be reinitialized for every new number 
    for j in range(len(str(i))):
        result= result + (pow(int(str(i)[j]),(len(str(i)))))
    if result==i:  # print outside the for loop since it will print the same number satisfying the if condition again
        print(result)
    i+=1