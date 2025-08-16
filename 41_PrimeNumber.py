while (True):
    number=input("Enter Number to check it is prime or Enter (a) to stop : ")
    if(number=="a"):
        break
    number=int(number)
    if(number<=1):
        print("Not Prime")
    else:
        for  i in range(2,number):
            if(number % i==0):
                print("Not Prime")
                break
        else:
            print("Prime Number")