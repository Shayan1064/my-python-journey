# Just printing number or string 
number =1
while number <=15:
    print(number,"I am learning Python")
   
    number+=1

# Practise Problem
# Print the multuplication table of N
num=1
print("Enter your number")
number=int(input("Number :"))
while num<=10:
    print(num*number)
    num+=1

#Loop in List

number=[1,4,9,16,25,36,49,64]
index=0
while index <=len(number):
    print("Index ",index," ",number[index])
    index+=1

#Searching in list
Number=[1,4,9,16,25,36,49,64]
idx=0
search=36

while idx <= len(Number):
    if(Number[idx]==search):
        print("The number is found at the index : ",idx)
        break
    idx+=1
else:
        print("NOT found")

      
    
