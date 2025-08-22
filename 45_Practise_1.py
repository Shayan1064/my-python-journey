# write a function to print out the greatest number...

def great(a,b,c):
    if(a > b and a > c):
        print("The greatest is : ",a)
    elif(b > a and b > c):
        print("The greatest is : ",b)
    else:
        print("The greatest is : ",c)

great(12,23,34)