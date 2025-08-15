

# write code that if student have 40% and must above 33 marks in each subject then print you are passed other wise he failed

marks1=int(input("Enter marks 1"))
marks2=int(input("Enter marks 2"))
marks3=int(input("Enter marks 3"))

# first i have to find percnetage of total

total=((marks1+marks2+marks3)/300)*100

if(total>=40 and marks1>=33 and marks2>=33 and marks3>=33):
    print("You are Passed")
else:
    ("Try again next year!")