#write function to count the length of list 

Cities=[1,2,3,4,5,6,7,8,9]

def length(L):
    print(len(L))

length(Cities)

# write a fuction to calculate the factorial

number=int(input("Number :"))
def factorial(number):
    fact=1
    for i in range(1,number+1):
        fact*=i
    print(fact)

factorial(number)

#write a function to convert the USD into PKR

print("Enter Rupee")
pkr=int(input())
def converter(rupee):
    print(rupee*280)

converter(pkr)