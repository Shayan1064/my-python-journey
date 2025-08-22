def factorial(number):
    if(number==1 or number==0):
        return 1
    return number*factorial(number-1)
number=int(input("Enter Number : "))
print("The factorial of this number is : ",factorial(number))


factorial(number)