

 # Write a fucntion to sum of natrual numbers like n+(n-1)+(n-2).....

def sum(number):
    if(number==1):
        return 1
    return sum(number-1)+number

print(sum(4))