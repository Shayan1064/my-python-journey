print("Welcome to Grading System")
print()
print("Please Enter Your name")
name=input()
print("Please Enter your marks")
marks=int(input())
print("This is your Grade ", name)

if(marks >=85 and marks <=100 ):
    print("A")
elif(marks >=70 and marks <=84):  
    print("B")
elif(marks >=60 and marks <=69):  
    print("C")
elif(marks >=55 and marks <=59):  
    print("D")
elif(marks >=50 and marks <=54):  
    print("D-")
else:
    print("Failed")